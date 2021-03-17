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
from jokes import get_joke
from calendar_ import Calendar

other_text = '🙂 Xin Chào. Tôi là Bot chat\
\n- tuvi <tuoi>: Xem tử vi theo tuổi\
\n- hoangdao <cung>: Xem cung hoàng đạo\
\n- lich: Xem lịch\
\n- thoitiet <thanhpho>: Xem thời tiết\
\n- covid: Xem thông tin dịch covid\
\n- joke: 1 mẩu truyện cười'\



class VoccerClient(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        sleep = random.randint(2, 5)

        if author_id != self.uid:
            time.sleep(sleep)
            if message_object.text:
                message_text = message_object.text.lower()

                if message_text == '/getid':
                    return self.send(Message(text=message_object.author),
                              thread_id=thread_id, thread_type=thread_type)

                elif 'tuvi' in message_text:
                    tuoi = message_text[message_text.index(
                        'tuvi') + len('tuvi'):]
                    tuvi = TuVi()
                    loi_phan = tuvi.con_giap(Cgiap=tuoi)
                    return self.send(Message(text=loi_phan),
                              thread_id=thread_id, thread_type=thread_type)
                elif 'hoangdao' in message_text:
                    cung = message_text[message_text.index(
                        'hoangdao') + len('hoangdao'):]
                    tuvi = TuVi()
                    loi_phan = tuvi.cung_hoang_dao(cung_hd=cung)
                    self.send(Message(text=loi_phan),
                              thread_id=thread_id, thread_type=thread_type)
                elif 'lich' in message_text:
                    calendar = Calendar()
                    self.send(Message(text=calendar.show_result()),
                              thread_id=thread_id, thread_type=thread_type)
                elif 'thoitiet' in message_text:
                    location = message_text[len('thoitiet'):].strip()
                    weather = get_weather(location)
                    return self.send(Message(text=weather),
                                     thread_id=thread_id,
                                     thread_type=thread_type
                                     )
                elif 'covid' in message_text:
                    infor = get_ncov()
                    return self.send(Message(text=infor),
                                     thread_id=thread_id,
                                     thread_type=thread_type
                                     )
                elif 'joke' in message_text:
                    joke = get_joke()
                    return self.send(Message(text=joke),
                                     thread_id=thread_id,
                                     thread_type=thread_type
                                     )
                else:
                    return self.send(Message(text=other_text),
                                     thread_id=thread_id,
                                     thread_type=thread_type
                                     )
            else:
                return self.send(Message(text=other_text),
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
