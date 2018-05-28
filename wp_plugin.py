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

driver = webdriver.Chrome(executable_path=str(Path('driver.exe').resolve()))
plugin_links = []
plugin_infos = []

for i in range(99):
    if i == 0:
        driver.get("https://wordpress.org/plugins/browse/popular/")
    else:
        driver.get("https://wordpress.org/plugins/browse/popular/page/"+str(i))

    anchors = driver.find_elements_by_css_selector("h2.entry-title a")

    for anchor in anchors:
        plugin_links.append(anchor.get_attribute("href"))

print(len(plugin_links))


for link in plugin_links:
    driver.get(link)
    name = driver.find_element_by_css_selector("h1.plugin-title").text

    try:
        author = driver.find_element_by_css_selector("a.url.fn.n").get_attribute("href")
    except NoSuchElementException:
        author = driver.find_element_by_css_selector("span.author.vcard").text

    tags = driver.find_elements_by_css_selector("div.tags a")
    tag_included = []
    for tag in tags:
        tag_included.append(tag.text)
    installation = driver.find_element_by_xpath("//*[contains(text(), 'Active installations: ')]").text.replace("Active installations: ", "").replace("+", "").replace(" million", "000000")
    last_updated = driver.find_element_by_xpath("//*[contains(text(), 'Last updated: ')]").text.replace("Last updated: ", "")

    info = {
        "Name": name,
        "Author": author,
        "Tags": "\n".join(tag_included),
        "Active installation": installation.split(":")[1],
        "Last updated": last_updated.split(":")[1],
        "URL" : link
    }

    plugin_infos.append(info)

pyexcel.save_as(records=plugin_infos, dest_file_name="plugin_info.xlsx")
