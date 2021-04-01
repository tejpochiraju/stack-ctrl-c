#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from random import randint
import pyperclip

def get_code():
    # These IDs seem to exist
    question_id = randint(11111, 9999999)
    url = "https://stackoverflow.com/questions/{}".format(question_id)
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    try:
        code = soup.find('code').get_text(strip=True)
        pyperclip.copy(code)
    except:
        get_code()

if __name__=="__main__":
    get_code()