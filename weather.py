# -*- coding: UTF-8 -*-
import requests

api_key = '6dcccf305d39905f92566e9e23a20c49'

def get_weather(location):
    location = location
    api_address = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=6dcccf305d39905f92566e9e23a20c49'.format(location)
    json_data = requests.get(api_address).json()
    if json_data['cod'] == 200:
        return "Thời Tiết ở {0} là: {1}\nNhiệt độ thấp nhất: {2}°C\nNhiệt độ cao nhất: {3}°C".format(json_data['name'], json_data['weather'][0]['main'], int(json_data['main']['temp_min']-273), int(json_data['main']['temp_max']-273))
    else:
        return 'Tên thành phố không hợp lệ'