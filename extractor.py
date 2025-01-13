from bs4 import BeautifulSoup
import requests 
import main

#url = 'https://www.bbc.com/news'              manual test
def scrape_data(link):
    scraped_data = []
    response = requests.get(link)
    if response.status_code == 200:
        #print(response.status_code)             # debugging statement
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all('h2')
        print(headlines)
        for headline in headlines:
            scraped_data.append(headline.text)
                    
    else:
        print(f"Failed to retireve the page. Status code : {response.status_code}")
    return scraped_data