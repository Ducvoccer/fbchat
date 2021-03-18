from bs4 import BeautifulSoup
import requests
import lxml


def get_ncov():
    url = 'https://ncov.moh.gov.vn/'
    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')

    numbers_tag = soup.find_all('span', class_='font24')
    numbers=[]
    for t in numbers_tag:
        numbers.append(t.get_text())
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
    