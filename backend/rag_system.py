import os

from langchain_ollama                   import ChatOllama, OllamaEmbeddings
from langchain.prompts                  import PromptTemplate
from langchain_core.documents           import Document
from langchain_community.vectorstores   import SKLearnVectorStore

import datasets_metadata    as dsmd
import preprocessing        as pp


DB_XMAS_PATH        = "./christmas_db"
DB_SUST_PATH        = "./sustainability_db"
K_RELEVANT_TABLES   = 3

def create_docs(dataset=dsmd.CHRISTMAS):
    """

    :param dataset: (dict) Dictionary containing metadata about dataset to process
    :return: (list[Document]) List of Document objects from processed dataset

    """
    questions   = dataset['QUESTIONS']
    groups      = dataset['GROUPS'].keys()

    doc_list    = []
    # For each question (group of rows)
    for q_number, q_text in questions.items():
        # One table per group (of columns)
        for group in list(groups)[1:]:
            # Full sample always + one group at a time
            criteria = f"the answers to: '{questions[group]}'" if group.startswith('Question') else f"{group}"
            doc_list.append(Document(page_content= (f"Main Question: **{q_text}**\n"
                                                    f"Sample groups based on: **{criteria}**"),
                                     # Save survey results for each description, in JSON serializable format
                                     metadata={'Question' : q_number, 'Group' : group}))

    return doc_list



xmas_dfs  = pp.process_dataset(dsmd.CHRISTMAS['PATH'])
sust_dfs  = pp.process_dataset(dsmd.SUSTAINABILITY['PATH'])

ollem = OllamaEmbeddings(model="llama3.2")

# Create or load DBs for vector stores, one for each dataset
if os.path.isfile(DB_XMAS_PATH):
    # Load documents from persisted vectorstore
    print('Loading Christmas db...')
    xmas_vs = SKLearnVectorStore(embedding=ollem, persist_path=DB_XMAS_PATH)
else:
    # Create embeddings for documents and store them in a vector store
    print('Creating Christmas db...')
    xmas_vs = SKLearnVectorStore.from_documents(documents=create_docs(),
                                                embedding=ollem,
                                                persist_path=DB_XMAS_PATH)
    xmas_vs.persist()

if os.path.isfile(DB_SUST_PATH):
    # Load documents from persisted vectorstore
    print('Loading Sustainability db...')
    sust_vs = SKLearnVectorStore(embedding=ollem, persist_path=DB_SUST_PATH)
else:
    # Create embeddings for documents and store them in a vector store
    print('Creating Sustainability db...')
    sust_vs = SKLearnVectorStore.from_documents(documents=create_docs(dsmd.SUSTAINABILITY),
                                                embedding=ollem,
                                                persist_path=DB_SUST_PATH)
    sust_vs.persist()


xmas_ret  = xmas_vs.as_retriever(search_kwargs={'k': K_RELEVANT_TABLES})
sust_ret  = sust_vs.as_retriever(search_kwargs={'k': K_RELEVANT_TABLES})

# Initialize the LLM with Llama 3.2 model
llama = ChatOllama(model="llama3.2", temperature=0)

# Define the prompt template for the LLM
instruction = ("# You are an analyst working with survey datasets that generates insightful responses.\n"
               "The following tables contain the survey data, each table containing answers to a main question.\n"
               "The possible answers are listed as rows, and the sample is divided into groups, listed as columns.\n"
               "Before each table there is an explanation of the main question asked an what the groups (columns) are.\n")
one_df_prompt = PromptTemplate(
    template=(
        "{instruction}\n\n"
        "## {description}\n"
        "{tables}\n"
        "**Generate insights regarding following question based only on the provided context:** "
        "{query}"
    ),
    input_variables=["instruction", "description", "tables", "query"]
)
compare_prompt = PromptTemplate(
    template=(
        "{instruction}\n\n"
        "## {xmas_des}\n"
        "{xmas_tables_text}\n"
        "## {sust_des}\n"
        "{sust_tables_text}\n\n"
        "**Generate insights by comparing the previous tables for following question:** "
        "{query}"
    ),
    input_variables=["instruction", "xmas_des", "xmas_tabs", "sustainability_des", "sustainability_tabs", "query"]
)

def retrieve_context(query: str, christmas=True) -> str:
    """
    Retrieve table data from DB based on query semantic search
    :param query: (str) Query to search on DB
    :param christmas: (bool) True if search for Christmas dataset, False for Sustainability dataset
    :return:
    """
    docs    = (xmas_ret    if christmas else sust_ret).invoke(query)
    dfs     = (xmas_dfs    if christmas else sust_dfs)

    # Obtain sub-tables containing info for 1 question and 1 group each
    tables  = [dfs[doc.metadata['Question']][['Sample'] + [doc.metadata['Group']]] for doc in docs]

    tables_text = ""
    for i in range(len(docs)):
        tables_text += f"{i + 1}. {docs[i].page_content}\n"
        tables_text += f"{pp.df_to_md(tables[i])}\n\n"

    return tables_text


def run_query(query: str, christmas=True, compare=False) -> str:
    """
    Runs query on an LLM

    :param query: (str) Query from user to base the generated insights on
    :param compare: (bool) If True, retrieve data from both datasets and tell LLM to compare
    :param christmas: (bool) If True and compare is False, retrieve data from Christmas dataset (sustainability if False)

    :return: LLM response stream
    """
    print('Retrieving...')
    if compare:
        xmas_tables_text = retrieve_context(query)
        sust_tables_text = retrieve_context(query, False)

        prompt_variables = {"instruction"       : instruction,
                            "xmas_des"          : dsmd.CHRISTMAS['DESCRIPTION'],
                            "xmas_tables_text"  : xmas_tables_text,
                            "sust_des"          : dsmd.SUSTAINABILITY['DESCRIPTION'],
                            "sust_tables_text"  : sust_tables_text,
                            "query"             : query}
        filled_prompt = compare_prompt.invoke(prompt_variables)

    else:
        tables_text = retrieve_context(query, christmas)
        description = (dsmd.CHRISTMAS if christmas else dsmd.SUSTAINABILITY)['DESCRIPTION']
        prompt_variables = {"instruction"   : instruction,
                            "description"   : description,
                            "tables"        : tables_text,
                            "query"         : query}
        filled_prompt = one_df_prompt.invoke(prompt_variables)

    for chunk in llama.stream(filled_prompt.to_string()):
        yield chunk.content

if __name__ == '__main__':
    for word in run_query("Can you tell me some differences in answer based on gender?"):
        print(word, end="", flush=True)
