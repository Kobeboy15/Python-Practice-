import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


url = 'http://localhost:8080/signup/'

browser = webdriver.Chrome('./chromedriver')
browser.get(url)

assert 'ApplyBPO' in browser.title

response = requests.get(url)
print(response)

wait = WebDriverWait(browser, 3)

# def inputFirstname(TextStuff):
#     elem = WebDriverWait(browser, 3).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "input"))
#     )
#     elem.send_keys(TextStuff + Keys.RETURN)


try:
    # inputFirstname('Hello How are you')
    items = browser.find_elements_by_tag_name('input')

    for item in items:

        try:
            item.send_keys('234234' + Keys.RETURN)

        except:
            print(item)

finally:
    print('HELLO THIS WORKS OMG')
    # browser.quit()
