document.getElementById('userInput').addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("sendButton").click();
  }
});

document.getElementById('sendButton').addEventListener('click', function() {
    const input = document.getElementById('userInput').value;
    const loader = document.getElementById("loader-id");
    if (input && loader == null) {
        // Check switches
        var xmas = document.getElementById("switch1").checked;
        var sust = document.getElementById("switch2").checked;

        if (xmas || sust) {
            document.getElementById('userInput').value = ''; // Clear the input
            showQuery("**" + input + "** " + ((xmas && sust) ? "<sup>[C+S]</sup>" : (xmas ? "<sup>[C]</sup>" : "<sup>[S]</sup>") ));

            if (xmas) {
                if (sust) {
                    postQueryBackend('http://localhost:8000/query/compare/', input);
                } else {
                    postQueryBackend('http://localhost:8000/query/christmas/', input);
                }
            } else {
                postQueryBackend('http://localhost:8000/query/sustainability/', input);
            }
        }
    }
});

async function postQueryBackend(url, message) {
    showLoader();

    const response = await fetch('http://localhost:8000/query/christmas/', {
        method: 'POST',
        keepalive: true,
        headers: {
            'Content-Type'  : 'application/json',
        },
        body: JSON.stringify({ "input_str" : message }),
    });
    const reader = response.body.pipeThrough(new TextDecoderStream()).getReader();
    let insights = "";
    const messageElement = document.createElement('div');

    while (true) {
        const {value, done} = await reader.read();
        if (done) break;
        
        hideLoader();

        insights = insights.concat(value);
        updateChatElement(messageElement, insights.concat(" ⬤"));
    }
    updateChatElement(messageElement, insights)
}

function hideLoader() {
    const loader = document.getElementById("loader-id");  
    const load_text = document.getElementById("load-text-id");
    if (loader) {loader.remove()}
    if (load_text) {load_text.remove()}
}

function showLoader() {
    const loaderElement = document.createElement('div');
    loaderElement.className = "loader";
    loaderElement.id = "loader-id";
    const loaderTextElement = document.createElement('div');
    loaderTextElement.className = "load-text";
    loaderTextElement.id = "load-text-id";

    updateChatElement(loaderElement, "");
    updateChatElement(loaderTextElement, "Analyzing...");
}

function showQuery(query) {
    const queryElement = document.createElement('div');
    queryElement.className = "user-message";

    updateChatElement(queryElement, query);

    const lineBreak = document.createElement('div');
    lineBreak.className = "line-break";
    updateChatElement(lineBreak, "");
}

function updateChatElement(messageElement, markdownContent) {
    // Convert markdown to HTML and append to the chat window
    const chatWindow = document.getElementById('chatWindow');
    const htmlContent = marked.parse(markdownContent);
    messageElement.innerHTML = htmlContent;
    chatWindow.appendChild(messageElement);
    chatWindow.scrollTop = chatWindow.scrollHeight; // Auto scroll to bottom
}
