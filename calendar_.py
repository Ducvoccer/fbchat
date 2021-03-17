import requests
import os
import datetime
from lunarcalendar import Converter, Solar, Lunar


class Calendar():
    def __init__(self):
        self.solar_today = datetime.date.today()
        self.lunar_today = Converter.Solar2Lunar(Solar(self.solar_today.year, self.solar_today.month, self.solar_today.day))
        try:
            r = requests.get('https://docs.google.com/document/u/0/export?format=txt&id=1b2aQMfZvhLhqs5bnGrdNZUnOSmCGsuNZeSH8Qk6ndrg&token=AC4w5VjlljBzAvNU8CtCSnvvFwe52p-2-w%3A1589941528767&ouid=102939292131381354747&includes_info_params=true&inspectorResult=%7B%22pc%22%3A1%2C%22lplc%22%3A20%7D')
            bir = r.text
            self.bir = bir
        except Exception as e:
            print(e)
    def show_result(self):
        text = 'Dương lịch: {}-{}-{}\nÂm lịch: {}-{}-{}'.format(\
        self.solar_today.day,self.solar_today.month, self.solar_today.year,self.lunar_today.day,self.lunar_today.month, self.lunar_today.year)
        info = self.check_birthday()
        if info:
            text += '\n**************\nHôm nay là sinh nhật của:'
            for i in info:
                text += '\n'
                age, name, type_ = i[0], i[1], i[2]
                if type_ == 'lunar':
                    text += '{} ở tuổi {} theo Âm lịch'.format(name, age, type_)
                else:
                    text += '{} ở tuổi {} theo Dương lịch'.format(name, age, type_)
        return text  
                    
    def check_birthday(self):
        p = self.bir.split('\n')
        if not p:
            print('not exist file')
            return

        self.solar_today = datetime.date.today()

        self.lunar_today = Converter.Solar2Lunar(
            Solar(self.solar_today.year, self.solar_today.month, self.solar_today.day))

        info = []
        for i in p:
            if i == '':
                continue
            name_birthday = i.split(':')[0]
            solar_birthday = i.split(':')[1].replace(' ', '')
            solar_day = int(solar_birthday.split('/')[0])
            solar_month = int(solar_birthday.split('/')[1])
            solar_year = int(solar_birthday.split('/')[2])

            # exception unknown
            if solar_day == 0:
                solar_day = 1
            if solar_month == 0:
                solar_month = 1
            if solar_year == 0:
                solar_year = 1900

            try:
                lunar_birthday = Converter.Solar2Lunar(
                    Solar(solar_year, solar_month, solar_day))
            except Exception as e:
                print(e)
                print(solar_year, solar_month, solar_day)

            if solar_day == self.solar_today.day and solar_month == self.solar_today.month:
                age = int(self.solar_today.year - solar_year)
                info.append([age, name_birthday, 'solar'])
            if lunar_birthday.day == self.lunar_today.day and lunar_birthday.month == self.lunar_today.month:
                age = int(self.lunar_today.year - lunar_birthday.year)
                info.append([age, name_birthday, 'lunar'])
        return info

