document.getElementById("askBtn").addEventListener("click", async () => {
    try {
        const question = document.getElementById("question").value;

        let [tab] = await chrome.tabs.query({
            active: true,
            currentWindow: true
        });

        const url = tab.url;

        document.getElementById("answer").innerText = "Thinking...";

        const res = await fetch("http://127.0.0.1:5000/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url,
                question: question
            })
        });

        console.log("Status:", res.status);

        const text = await res.text();

        console.log("Raw Response:", text);

        const data = JSON.parse(text);

        document.getElementById("answer").innerText = data.answer;

    } catch (err) {
        console.error(err);
        document.getElementById("answer").innerText = "Error: " + err.message;
    }
});