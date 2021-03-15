import requests
import os
from datetime import date


class Birthday():
    def __init__(self):
        try:
            r = requests.get(
                'https://docs.google.com/document/u/4/export?format=txt&id=1MaetdIy3yDCVHEzmD87SGyHquNavWJo3k-RVU7tYE6Q&token=AC4w5Vg4qq7bqDhwXOwmXKAyzpZr7afLzg%3A1586228079190&includes_info_params=true')
            b = r.text
            with open('birthday', 'w') as f:
                f.write(b)
        except Exception as e:
            print(e)

    def get_time_now(self):
        today = date.today()
        today = today.strftime("%d/%m/%Y")
        day = today.split('/')[0]
        month = today.split('/')[1]
        year = today.split('/')[2]

        return day, month, year

    def check_birthday(self):
        with open('birthday', 'r') as f:
            birthday = f.read().split('\n')
        for b in birthday:
            if b == '':
                continue
            else:
                name = b.split(':')[0].strip()
                date = b.split(':')[1].replace(' ', '')
