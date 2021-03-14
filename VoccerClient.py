# -*- coding: UTF-8 -*-
from fbchat.models import *
from fbchat import log, Client
import datetime
from tu_vi import TuVi
from lunarcalendar import Converter, Solar, Lunar
import random
import time
from weather import get_weather
from ncov import get_ncov


other_text = '🙂 Xin Chào. Tôi là Bot chat của Trong Duc - Voccer.\n- Hiện tại anh ấy không thể rep tin nhắn ngay được.\
\n- Xem tử vi gõ /tuvi <tuổi>\nví dụ: /tuvi sửu. \n- Xem cung hoàng đạo gõ /hoangdao <cung>\
\nví dụ: /hoangdao song ngư\n- Xem lịch gõ /lich\
\n- Xem thời tiết /thoitiet <thành phố>\
\nví dụ: /thoitiet hà nội '



class VoccerClient(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        sleep = random.randint(2, 5)

        if author_id != self.uid:
            if message_object.text:
                if message_object.text == '/Getid' or message_object.text == '/getid':
                    self.send(Message(text=message_object.author),
                              thread_id=thread_id, thread_type=thread_type)

                elif '/tuvi' in message_object.text:
                    tuoi = message_object.text[message_object.text.index(
                        '/tuvi') + len('/tuvi'):]
                    tuvi = TuVi()
                    loi_phan = tuvi.con_giap(Cgiap=tuoi)
                    self.send(Message(text=loi_phan),
                              thread_id=thread_id, thread_type=thread_type)
                elif '/hoangdao' in message_object.text:
                    cung = message_object.text[message_object.text.index(
                        '/hoangdao') + len('/hoangdao'):]
                    tuvi = TuVi()
                    loi_phan = tuvi.cung_hoang_dao(cung_hd=cung)
                    self.send(Message(text=loi_phan),
                              thread_id=thread_id, thread_type=thread_type)
                elif '/lich' in message_object.text:
                    solar_today = datetime.date.today()
                    lunar_today = Converter.Solar2Lunar(
                        Solar(solar_today.year, solar_today.month, solar_today.day))
                    self.send(Message(text="Hôm nay, \nDương lịch: {}-{}-{}\nÂm lịch: {}-{}-{}".format(solar_today.day, solar_today.month, solar_today.year, lunar_today.day, lunar_today.month, lunar_today.year)),
                        thread_id=thread_id,
                        thread_type=thread_type
                    )
                elif '/thoitiet' in message_object.text:
                    location = message_object.text[len('/thoitiet'):].strip()
                    weather = get_weather(location)
                    return self.send(Message(text=weather),
                        thread_id=thread_id,
                        thread_type=thread_type
                    )
                elif '/ncov' in message_object.text:
                    infor = get_ncov()
                    return self.send(Message(text=infor),
                        thread_id=thread_id,
                        thread_type=thread_type
                    )
                else:
                    time.sleep(sleep)
                    self.send(Message(text=other_text),
                              thread_id=thread_id,
                              thread_type=thread_type
                              )
            else:
                time.sleep(sleep)
                self.send(Message(text=other_text),
                          thread_id=thread_id,
                          thread_type=thread_type
                          )

    def listen_custom(self, markAlive=None):
        global time_start

        if markAlive is not None:
            self.setActiveStatus(markAlive)

        self.startListening()
        self.onListening()

        while True:
            if not self.listening or not self.doOneListen():
                break       
        self.stopListening()
