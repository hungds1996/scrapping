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

driver = webdriver.Chrome(executable_path=str(Path('driver.exe').resolve()))

driver.get('https://chrome.google.com/webstore/category/ext/10-blogging?hl=en-US')

driver.execute_script("window.open('about:black', 'tab2')")
def to_tab(idx):
    driver.switch_to_window(driver.window_handles[idx -1])

to_tab(1)

for i in range(2):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(2)

extensions = driver.find_elements_by_css_selector("div.h-a-x a.a-u")
extension_links = []
for extension in extensions:
    extension_link = extension.get_attribute('href')
    extension_links.append(extension_link)

for link in extension_links:
    to_tab(2)
    driver.get(link)
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "pre.C-b-p-j-Oa")))
    des = driver.find_element_by_css_selector("pre.C-b-p-j-Oa")
    print(des.text)
    time.sleep(1)

# to_tab(2)
#
# for link in extension_links:
#     driver.get(extension_link)
#
#     WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "pre.C-b-p-j-Oa")))
#     des = driver.find_element_by_css_selector("pre.C-b-p-j-Oa")
#     print(des.text)
