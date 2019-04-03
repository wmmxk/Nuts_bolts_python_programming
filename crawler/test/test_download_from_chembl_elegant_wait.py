""" This solution is more elegant
    the waiting time is not hard-coded this time.
"""

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_download_from_chembl():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.ebi.ac.uk/chembl/g/#browse/activities/filter/target_chembl_id%3ACHEMBL5455")

    csvLink = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-format='CSV']")))
    csvLink.click()
    # wait for the download link and click
    hereLink = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".BCK-download-messages-container .BCK-download-link-container a")))
    hereLink.click()
    time.sleep(20)