
from selenium import webdriver
import time


def test_facebook_log():

    driver = webdriver.Chrome()
    driver.get("http://mutationdb.com/database")

    download_btn = driver.find_element_by_xpath("""//*[@id="mol-table_wrapper"]/div[1]/a[1]""")
    print("download:", download_btn)
    download_btn.click()

    time.sleep(3)

