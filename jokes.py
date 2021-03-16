from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time 

CHROMEDRIVER_PATH = './chromedriver'

chrome_options = Options()

chrome_options.add_argument("--headless")

browser = webdriver.Chrome(executable_path='./chromedriver',options=chrome_options)

def get_joke():
        
    browser.get('https://www.cuoibebung.com/')
    joke_contents = ''

    while True:
        joke_elements =  browser.find_elements_by_xpath('//div[@class="entry-content"]')[1]
        if joke_elements.is_displayed():
            break 
    
    joke_p = joke_elements.find_elements_by_tag_name('p')
    result = ''
    for p in joke_p:
        result = result + p.text + '\n'
    return result


