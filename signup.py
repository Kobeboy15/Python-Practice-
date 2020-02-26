import requests
import os
import random
from random import randint
import string
import json


chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
url = 'http://localhost:8000/api-sileo/applybpo/applicant-onboarding/create/'


names = json.loads(open('names.json').read())

isTrue = True

while isTrue:
    for name in names:
        name_extra = ''.join(random.choice(string.digits))

        phnumber_start = '92783'
        phnumber_extra = ''.join(["{}".format(randint(0,9)) for num in range(0, 5)])

        email = name.lower() + name_extra + '@yahoo.com'
        passw = ''.join(random.choice(chars) for i in range(10))

        phnumber = phnumber_start + phnumber_extra

        payload = {
            'email': email,
            'user_name': name_extra,
            'first_name': name,
            'last_name': name,
            'password': passw,
            'confirmation': passw,
            'phone_country_code': '63',
            'phone_number': phnumber,
            'salary_expectation': 40000,
            'preferred_currency': 'PHP',
            'position': 5,
            'freelance': 'false',
            'focuses': 8,
            'sub_specialties': 10,
            'job_locations': 2,
            'birth_date': '1998-07-07',
            'region': 'Asia/Manila'
        }

        try:
            print(type(phnumber) is str)
            response = requests.post(url, allow_redirects=False, data=json.dumps(payload))
            print(response)
            print('Sending')
        except:
            print ('He locked you out')
            isTrue = False
            break
