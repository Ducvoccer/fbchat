from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime
class Covid():
    def __init__(self):
        self.url_main = 'https://ncov.moh.gov.vn/'
        self.url_notify = 'https://ncov.moh.gov.vn/vi/web/guest/dong-thoi-gian'

    def get_news(self):
        res = requests.get(self.url_notify, verify=False)
        soup = BeautifulSoup(res.content, 'lxml')
        time_lines = []
        titles = []
        contents = []
        posts = soup.find_all('div', {'class': 'timeline-detail'})
        for p in posts:
            time_line = p.find('div', {'class': 'timeline-head'}).find('h3').get_text()
            date = time_line.split(' ')[1]
            day = date.split('/')[0]
            month = date.split('/')[1]
            year = date.split('/')[2]
            day = 20
            if (int(day) == datetime.now().day and int(month) == datetime.now().month and int(year) == datetime.now().year):
                title = p.find('div', {'class': 'timeline-content'}).find_all('p')[1].get_text()
                content = p.find('div', {'class': 'timeline-content'}).find_all('p')[2].get_text()
                time_lines.append(time_line)
                titles.append(title)
                contents.append(content)
        return time_lines, titles, contents

    def get_number_ncov(self):
        res = requests.get(self.url_main, verify=False)
        soup = BeautifulSoup(res.content, 'lxml')
        numbers_tag = soup.find_all('span', class_='font24')
        numbers=[]
        for t in numbers_tag:
            numbers.append(t.get_text())
        ncov_info = \
        'Việt Nam:\n'\
        '\tSố ca nhiễm: {0}\n'\
        '\tĐang điều trị: {1}\n'\
        '\tKhỏi: {2}\n'\
        '\tTử Vong: {3}\n'\
        'Thế giới:\n'\
        '\tSố ca nhiễm: {4}\n'\
        '\tĐang điều trị: {5}\n'\
        '\tKhỏi: {6}\n'\
        '\tTử Vong: {7}\n'.format(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], numbers[6], numbers[7])
        return ncov_info
    