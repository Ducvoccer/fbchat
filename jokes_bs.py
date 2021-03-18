from bs4 import BeautifulSoup
import requests
import lxml


def get_joke():
    url = 'https://www.cuoibebung.com/'
    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')

    content_tag = soup.find_all('div', class_='entry-content')[1].find_all('p')
    results = ''
    for t in content_tag:
        results = results + '\n' + t.get_text() 
    return results
    