import pandas               as pd
import datasets_metadata    as dsmd


def process_dataset(file_path: str) -> dict:
    """
    Process dataset received as argument

    Parameters:
        file_path   (str)   : The path to an xlsx file with data from a consumer survey

    Returns:
        dict(str -> pd.DataFrame)  : A processed version of the dataframe, split into chunks for each question
    """
    df = pd.read_excel(file_path, header=None, keep_default_na=False)  # Do not convert into NaN
    survey = (dsmd.CHRISTMAS if file_path.endswith('christmas_dataset.xlsx') else dsmd.SUSTAINABILITY)

    # Discard all rows and columns without any info
    df = df.replace(['', ' '], None) # Replace spaces with NaN
    df = df.dropna(axis='index', how='all')
    df = df.dropna(axis='columns', how='all')

    # Discard unwanted info
    if survey == dsmd.CHRISTMAS:
        df  = df.iloc[:-10, :-3]                         # Discard Segments (christmas dataset)
        df  = df.loc[:, df.iloc[1,:] != 'No Group']      # Discard 'No Group' column (Question 5 - christmas)
    else:
        df  = df.loc[:, df.iloc[1,:] != 'Other']         # Discard 'Other' column (Question 16 - sustainability)
    df      = df.iloc[2:]                                # Discard two first rows (index)
    df      = df.drop(df[df.iloc[:,0].isna()].index)     # Drop percentages rows
    total   = df[df.iloc[:,0] == 'Total']                # Select rows with total group sizes
    df      = df.drop(total.index)                       # Drop redundant info

    # Create list of sub-dataframes, one per question
    question_dataframes = {}
    question_names      = list(survey['QUESTIONS'].keys())
    for current_q, next_q in zip(question_names, question_names[1:] + [None]):
        # Truncate dataframe to include only current question
        start  = df[df.iloc[:,0].str.startswith(current_q)].index[0]  # Row where current question starts
        if next_q is not None:
            end    = df[df.iloc[:,0].str.startswith(next_q)].index[0] # Row where next question starts
            tmp    = df.loc[start + 1 : end - 1] # Select question rows excluding questions themselves
        else:
            tmp    = df.loc[start + 1 : ]  # Last question

        # Re-escalate data into percentages: divide by total, multiply by 100
        tmp     = tmp.iloc[:, 1:] # Discard first column
        if not (survey == dsmd.SUSTAINABILITY and current_q in {'Question 1', 'Question 14'}):
            tmp = tmp.div(total.iloc[0, 1:]).mul(100).round().astype(int).astype(str).add('%')

        # Set index as question categories, columns as participants groups
        column_tuples   = [(criteria, group) for criteria, groups_list in survey['GROUPS'].items() for group in groups_list]
        tmp.columns     = pd.MultiIndex.from_tuples(column_tuples, name=survey['GROUPS_LEVEL_NAMES'])
        tmp.index       = pd.MultiIndex.from_product(survey['ANSWERS'][current_q])

        question_dataframes[current_q] = tmp

    return question_dataframes

def df_to_md(df: pd.DataFrame) -> str:
    """
    Convert multi-indexed dataframe into a simple Markdown table for LLM processing
    :param df: DataFrame to convert to string
    :return: Markdown version of the dataframe
    """
    copy = df.copy()
    copy.columns   = [" : ".join(col) for col in copy.columns.to_flat_index()]
    copy.index     = [" : ".join(row) for row in copy.index.to_flat_index()]
    return copy.to_markdown(tablefmt='grid')


if __name__ == '__main__':
    processed = process_dataset('christmas_dataset.xlsx')['Question 1'][['Sample', 'Gender']]

    print(processed)
