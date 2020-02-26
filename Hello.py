import requests
import os
from bs4 import BeautifulSoup
import random
import string
import json


chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
url = 'http://localhost:8000/signin/'


names = json.loads(open('names.json').read())

isTrue = True

while isTrue:
    for name in names:
        name_extra = ''.join(random.choice(string.digits))

        user = name.lower() + name_extra + '@yahoo.com'
        passw = ''.join(random.choice(chars) for i in range(8))

        payload = {"data": {'username': user,'password': passw }}

        try:
            requests.post(url, allow_redirects=False, data=json.dumps(payload))
            print ('Sending username %s and password %s' % (user, passw))

        except:
            print ('He locked you out')
            isTrue = False
            break

