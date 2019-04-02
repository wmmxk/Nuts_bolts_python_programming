from selenium.webdriver.common.keys import Keys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd


def test_sanity():
    options = Options()
    options.add_argument("--disable-infobars")

    browser = webdriver.Chrome()

    browser.get("https://www.ebi.ac.uk/chembl/g/#browse/activities/filter/target_chembl_id%3ACHEMBL5455")

    download = browser.find_element_by_id("GladosMainContent")
    download = browser.find_elements_by_xpath(""".//*[@id="GladosMainContent"]/div/div""")
    download = browser.find_element_by_css_selector('div.buttons-container')
    print(download)

    time.sleep(3)