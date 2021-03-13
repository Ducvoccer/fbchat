# -*- coding: utf-8 -*- 
import json
from VoccerClient import VoccerClient
import time
import sys

# import logging
# logging.basicConfig(level=logging.DEBUG)

email = 'phimtonghop37@gmail.com'
email = 'duc.nt161113@sis.hust.edu.vn'
password = ''
# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"

with open('flag', 'r') as f:
    flag = (int)(f.read())
    if flag == 1:
        sys.exit()
    else:
        with open('flag', 'w') as f:
            f.write('1')

# Load session đăng nhập từ trước nếu co
session_cookies = ''
try:
    with open('session_gen_{}.json'.format(email)) as f:
        session_cookies = json.load(f)
except Exception as e:
    print(e)

client = VoccerClient(email, password, user_agent=user_agent, session_cookies=session_cookies)

client.listen_custom(markAlive=False)