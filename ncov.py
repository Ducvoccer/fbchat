from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time


CHROMEDRIVER_PATH = './chromedriver'

chrome_options = Options()

chrome_options.add_argument("--headless")

browser = webdriver.Chrome(
    executable_path=CHROMEDRIVER_PATH, options=chrome_options)

def get_ncov():
    browser.get('https://ncov.moh.gov.vn/')
    while True:
        number_elements =  browser.find_elements_by_xpath('//span[@class="font24"]')
        if len(number_elements) > 0 and number_elements[0].is_displayed():
            break
    numbers = [e.text for e in number_elements if e.text]
    # browser.quit()
    ncov_info = '\
Việt Nam:\n\
\tSố ca nhiễm: {0}\n\
\tĐang điều trị: {1}\n\
\tKhỏi: {2}\n\
\tTử Vong: {3}\n\
Thế giới:\n\
\tSố ca nhiễm: {4}\n\
\tĐang điều trị: {5}\n\
\tKhỏi: {6}\n\
\tTử Vong: {7}\n'.format(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], numbers[6], numbers[7])
    return ncov_info