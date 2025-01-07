chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.htmlContent) {
        const resultsDiv = document.getElementById('results');
        const data = message.htmlContent;

        data.forEach(item => {
            const resultDiv = document.createElement('div');
            resultDiv.className = 'result';
            resultDiv.innerHTML = `
                <h2>${item.title}</h2>
                <p>${item.content}</p>
                <p><strong>Sentiment:</strong> ${item.sentiment}</p>
            `;
            resultsDiv.appendChild(resultDiv);
        });
    }
});
