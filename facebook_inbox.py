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

import pyexcel

driver = webdriver.Chrome(executable_path=str(Path('driver.exe').resolve()))

driver.get("http://facebook.com")
cookies = [
    {'domain': '.facebook.com', 'expiry': 1589619278.831347, 'httpOnly': True, 'name': 'sb', 'path': '/', 'secure': True, 'value': 'QkP9WgyDvr9gpWvXaXgmdFdB'}, 
    {'domain': '.facebook.com', 'expiry': 1527152122, 'httpOnly': False, 'name': 'wd', 'path': '/', 'secure': True, 'value': '1034x611'}, 
    {'domain': '.facebook.com', 'expiry': 1534323278.831376, 'httpOnly': False, 'name': 'c_user', 'path': '/', 'secure': True, 'value': '100000253275373'}, 
    {'domain': '.facebook.com', 'httpOnly': False, 'name': 'presence', 'path': '/', 'secure': True, 'value': 'EDvF3EtimeF1526547314EuserFA21B00253275373A2EstateFDutF1526547314102Et3F_5b_5dElm3FnullEutc3F0CEchFDp_5f1B00253275373F2CC'}, 
    {'domain': '.facebook.com', 'expiry': 1589619278.831192, 'httpOnly': True, 'name': 'datr', 'path': '/', 'secure': True, 'value': 'QkP9WhcOsl-74ZO71F4OogXL'}, 
    {'domain': '.facebook.com', 'expiry': 1534323278.831404, 'httpOnly': True, 'name': 'xs', 'path': '/', 'secure': True, 'value': '33%3ABGZ9fJCpY4gi2w%3A2%3A1526547287%3A14444%3A6382'}, 
    {'domain': '.facebook.com', 'expiry': 1534323283.108345, 'httpOnly': True, 'name': 'fr', 'path': '/', 'secure': True, 'value': '0FLwTqCfLH9hbihvG.AWW1F6yrkMbEpZC0nKq7aQZjgK4.Ba_UNC.a5.Fr9.0.0.Ba_UNc.AWX9XGJc'}, 
    {'domain': '.facebook.com', 'expiry': 1534323278.831463, 'httpOnly': True, 'name': 'pl', 'path': '/', 'secure': True, 'value': 'n'}, 
    {'domain': '.facebook.com', 'httpOnly': False, 'name': 'act', 'path': '/', 'secure': True, 'value': '1526547324232%2F2'}
]

for cookie in cookies:
    driver.add_cookie(cookie)

input("continue?")





# cookies = driver.get_cookies()

# f = open('myfile.txt', 'w')
# f.write(str(cookies))
# f.close()