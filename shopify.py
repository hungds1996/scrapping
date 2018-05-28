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

links = []
tool_infos = []

for i in range(5):
    if i == 0:
        driver.get("https://apps.shopify.com/categories/social-media")
    else:
        driver.get("https://apps.shopify.com/categories/social-media" + str(i))

    anchors = driver.find_elements_by_css_selector("a.appcard-overlay")

    for a in anchors:
        links.append(a.get_attribute("href"))

for link in links:
    driver.get(link)

    try:
        developer = driver.find_element_by_xpath("//td[contains(text(), 'Developer')]/following-sibling::td[1]").text
    except NoSuchElementException:
        developer = ""

    try:
        email = driver.find_element_by_xpath("//td[contains(text(), 'Email')]/following-sibling::td[1]").text
    except NoSuchElementException:
        emial = ""

    try:
        website = driver.find_element_by_xpath("//td[contains(text(), 'Website')]/following-sibling::td[1]").text
    except NoSuchElementException:
        website = ""

    try:
        phone = driver.find_element_by_xpath("//td[contains(text(), 'Phone')]/following-sibling::td[1]").text
    except NoSuchElementException:
        phone = ""

    name = driver.find_element_by_css_selector("div.app-header__details h1").text
    selling_points = driver.find_element_by_css_selector("div.app-selling-points.p30 ul").text

    tool_info = {
        "Name" : name,
        "Developer" : developer,
        "Email" : email,
        "Website" : website,
        "Phone" : phone,
        "Selling points" : selling_points
    }

    tool_infos.append(tool_info)

pyexcel.save_as(records=tool_infos, dest_file_name="shopify_tool.xlsx")
