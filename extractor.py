from bs4 import BeautifulSoup
import requests 

url = 'https://www.bbc.com/news'
scraped_data = []
response = requests.get(url)
if response.status_code == 200:
    #print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('h2')
    for headline in headlines:
        scraped_data.append(headline.text)
      
        
else:
    print(f"Failed to retireve the page. Status code : {response.status_code}")