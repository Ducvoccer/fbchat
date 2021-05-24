# -*- coding: utf-8 -*- 
import json
from json.decoder import JSONDecodeError
from VoccerClient import VoccerClient
import time
import sys

# import logging
# logging.basicConfig(level=logging.DEBUG)
list_emails = ['phimtonghop37@gmail.com', 'duc.nt161113@sis.hust.edu.vn', 'voccer.it@gmail.com']
email = list_emails[1]
password = ''
# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0"


with open('session/session_{}.json'.format(email)) as f:
    cookiesjar = dict()

    for i in json.load(f):
        cookiesjar[i["name"]] = i["value"]
    session_cookies = cookiesjar


if session_cookies:
    client = VoccerClient(email, password, user_agent=user_agent, session_cookies=session_cookies)
    client.listen_custom(markAlive=False)