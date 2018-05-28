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

driver.get("https://chrome.google.com/webstore/category/extensions?hl=en-US")

infos = []

for i in range(15):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(2)

extensions = driver.find_elements_by_css_selector("div.h-a-x a.a-u")
extension_links = []
for extension in extensions:
    extension_link = extension.get_attribute('href')
    extension_links.append(extension_link)

print(len(extension_links))
for i, link in enumerate(extension_links):
    if i > 216:
        driver.get(link)
        
        try:
            WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.C-b-p-j.C-b-p-j-Wd.Ka-Ia-j")))
        except TimeoutException:
            continue

        all_text = driver.find_element_by_tag_name("body").text.split()
        
        try:
            name = driver.find_element_by_css_selector("h1.e-f-w").text            
        except NoSuchElementException:
            name = ""

        try:            
            sales = int(driver.find_element_by_css_selector("span.e-f-ih").text.split()[0].replace(",","").replace("+",""))            
        except NoSuchElementException:
            sales = ""

        try:
            author = driver.find_element_by_css_selector(".e-f-Me").text[11:]
        except NoSuchElementException:
            author = ""

        try:
            version = driver.find_element_by_css_selector("span.C-b-p-D-Xe.h-C-b-p-D-md").text
        except NoSuchElementException:
            version = ""

        try:
            updated = driver.find_element_by_css_selector("span.C-b-p-D-Xe.h-C-b-p-D-xh-hh").text
        except NoSuchElementException:
            updated = ""

        description = driver.find_element_by_css_selector("div.C-b-p-j-Pb").text
        web = []
        contact = []
        
        for word in all_text:
            if len(word) < 3:
                pass
            if "@" in word and "." in word:
                contact.append(word.replace("?",""))
            if "http" in word or "www" in word:
                web.append(word.replace("?",""))
        
        info = {
            "Name" : name,
            "Sales" : sales,
            "Description" : description,
            "Websites" : '\n'.join(web),
            "Contacts" : '\n'.join(contact),
            "Author" : author,
            "Version" : version,
            "Updated" : updated,
        }
        infos.append(info)
        print(str(i) + name)
        print("-------------------------------")

pyexcel.save_as(records=infos, dest_file_name='ChromeExtension_recom.xlsx')
