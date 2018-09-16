from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome('{}/chromedriver'.format(BASE_DIR), chrome_options=options)


def get_html(url):
    driver.get(url)

    for a in driver.find_elements_by_css_selector('a'):
        if a.get_attribute('jsname') == 'Hly47e':
            a.click()

    time.sleep(0.5)

    view_details_div = driver.find_element_by_class_name('fnLizd')
    return view_details_div.get_attribute('innerHTML')
