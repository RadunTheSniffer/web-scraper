chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.htmlContent) {
        const resultsDiv = document.getElementById('results');
        const data = message.htmlContent;

        data.forEach(item => {
            const resultDiv = document.createElement('div');
            resultDiv.className = 'result';
            resultDiv.innerHTML = `
                <pre>${item}</pre>
            `;
            resultsDiv.appendChild(resultDiv);
        });
    }
});

