document.getElementById('sentimentForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const link = document.getElementById('link').value;
    const posts = document.getElementById('post').value;

    console.log('Form submitted:', { link, posts });

    try {
        const response = await fetch('http://localhost:5000/scraper', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ link, posts })
        });

        const responseData = await response.json();
        console.log('Response data:', responseData);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        chrome.tabs.create({ url: 'result.html' }, function (tab) {
            chrome.tabs.onUpdated.addListener(function (tabId, info) {
                if (info.status === 'complete' && tabId === tab.id) {
                    chrome.tabs.sendMessage(tabId, { htmlContent: responseData });
                }
            });
        });
    } catch (error) {
        console.error('Error:', error);
        alert(`Error: ${error.message}`);
    }
});
