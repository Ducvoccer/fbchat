# -*- coding: UTF-8 -*-
from fbchat import Client
from fbchat.models import *
import time
import random

other_text = '🙂 Xin Chào. Tôi là Bot chat của Trong Duc - Voccer. \n- Hiện tại anh ấy không thể rep tin nhắn ngay được. \n- Nếu xem tử vi gõ /tuvi <tuổi>; ví dụ: /tuvi sửu. \n-Nếu xem cung hoàng đạo gõ /hoangdao <cung>; \n ví dụ: /hoangdao song ngư\n- xem lịch gõ /lich'

time_start = time.time()

class VoccerClient(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        sleep = random.randint(2, 10)
        if author_id != self.uid:
            time.sleep(sleep)
            self.send(Message(text=other_text),
                      thread_id=thread_id,
                      thread_type=thread_type)
    def listen_custom(self, markAlive=None):
        if markAlive is not None:
            self.setActiveStatus(markAlive)

        self.startListening()
        self.onListening()

        while True:
            if not self.listening or not self.doOneListen():
                break    
        self.stopListening()
