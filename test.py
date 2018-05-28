import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import json

import pyexcel

def scrap_number(css_selector):
    return int(driver.find_element_by_css_selector(css_selector).text.replace(",","").split(' ')[0])

driver = webdriver.Chrome(executable_path=str(Path('driver.exe').resolve()))

cookies = [{'domain': '.customer.io', 'expiry': 1535441531, 'httpOnly': False, 'name': 'cioFT', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.customer.io', 'expiry': 1535441531, 'httpOnly': False, 'name': 'cioLT', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': 'fly.customer.io', 'httpOnly': True, 'name': '_session', 'path': '/', 'secure': False, 'value': 'BAh7CUkiD3Nlc3Npb25faWQGOgZFVEkiJTc3ZGZmZGQ5MzEyY2RlOTNlNzc0OTZmMTJjYzAyOGY2BjsAVEkiCmZsYXNoBjsAVHsHSSIMZGlzY2FyZAY7AFRbBkkiCmFsZXJ0BjsARkkiDGZsYXNoZXMGOwBUewZJIgphbGVydAY7AEZJIh9JbnZhbGlkIGVtYWlsIG9yIHBhc3N3b3JkLgY7AFRJIhl3YXJkZW4udXNlci51c2VyLmtleQY7AFRbB1sGaQOeSwFJIiIkMmEkMTAkbERxRWxtOXVCZU9mOXhhUEhZcjhndQY7AFRJIh13YXJkZW4udXNlci51c2VyLnNlc3Npb24GOwBUewZJIiNuZWVkX3R3b19mYWN0b3JfYXV0aGVudGljYXRpb24GOwBURg%3D%3D--dbb28c98cab968cac50fca86e369bf07abb363a6'}, {'domain': '.customer.io', 'expiry': 1527579137, 'httpOnly': False, 'name': '_cio', 'path': '/', 'secure': False, 'value': '849da6b9-31c2-0e90-8304-57d8e6f5e245'}, {'domain': '.customer.io', 'expiry': 1527494657, 'httpOnly': False, 'name': '_sp_ses.5fe6', 'path': '/', 'secure': False, 'value': '*'}, {'domain': '.customer.io', 'expiry': 1527579225, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.811495723.1527492737'}, {'domain': '.customer.io', 'expiry': 1527492887, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.customer.io', 'expiry': 1590564825, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1239202927.1527492737'}, {'domain': '.customer.io', 'expiry': 1559028825, 'httpOnly': False, 'name': 'ajs_group_id', 'path': '/', 'secure': False, 'value': 'null'}, {'domain': '.customer.io', 'expiry': 1559028826, 'httpOnly': False, 'name': 'ajs_user_id', 'path': '/', 'secure': False, 'value': '%2236806%22'}, {'domain': 'fly.customer.io', 'httpOnly': False, 'name': '_access', 'path': '/', 'secure': False, 'value': 'M2Y5ZGIyN2U5M2IwNjFhZjk5OWFiMmM1N2ZjYWIzNWRiMTVhYTJmMzQyZDUxYTU4NDJkZTNhZDJmYTc2'}, {'domain': '.customer.io', 'expiry': 1559028826, 'httpOnly': False, 'name': 'ajs_anonymous_id', 'path': '/', 'secure': False, 'value': '%22dc73984b-864d-4645-a735-7084a7c9fec2%22'}, {'domain': '.customer.io', 'expiry': 1590564857, 'httpOnly': False, 'name': '_sp_id.5fe6', 'path': '/', 'secure': False, 'value': '413134780691a662.1527492737.1.1527492857.1527492737.d9f29cc3-ad2d-4d60-8228-dedad9ec55d6'}]

driver.get("https://customer.io/")

for cookie in cookies:
    driver.add_cookie(cookie)

stats = []

driver.get("https://fly.customer.io/env/70328/campaigns/13/overview")

WebDriverWait(driver, timeout=50).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="ember1371"]/dl/dt''')))

sent = int(driver.find_element_by_css_selector('.cio-metric-summary__sent.ember-view dl dt').text.replace(",",""))
spam = scrap_number('.cio-metric-summary__spam.ember-view dd')
unsubscribed = scrap_number('.cio-metric-summary__unsubscribed.ember-view dd')
bounced = scrap_number('.cio-metric-summary__bounced.ember-view dd')
surpressed = scrap_number('.cio-metric-summary__suppressed.ember-view dd')

stat = {
    "Sent" : sent,
    "Spam" : spam,
    "Unsubscribed" : unsubscribed,
    "Bounced" : bounced,
    "Surpressed" : surpressed
}

stats.append(stat)

pyexcel.save_as(records=stats, dest_file_name="test.xlsx")