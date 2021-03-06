import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions


def test_download_from_chembl():
    """
    set the download path on the fly;
    open the chrome driver
    open the url in the driver
    find the click for csv
    click the csv button
    then download

    """
    chrome_driver_path = "/usr/local/bin/chromedriver"

    options = ChromeOptions()
    prefs = {"download.default_directory": "/home/wxk/Downloads/stock/"}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(chrome_options=options)# ,executable_path=chrome_driver_path)

    driver.get("https://www.ebi.ac.uk/chembl/g/#browse/activities/filter/target_chembl_id%3ACHEMBL5455")
    # wait 5 seconds for the website to load, otherwise the code will fail
    time.sleep(5)
    # find by css selector also works
    # driver.find_element_by_css_selector("[data-format='CSV']").click()
    click1 = driver.find_element_by_xpath("""//*[@id="GladosMainContent"]/div/div/div[1]/div[2]/div[1]/div[3]/div/a[1]""")
    click1.click()

    # wait for loading:
    time.sleep(5)
    #driver.find_element_by_css_selector(".BCK-download-messages-container.BCK-download-link-container a").click()

    click2 = driver.find_element_by_xpath("""//*[@id="GladosMainContent"]/div/div/div[1]/div[2]/div[2]/div/div/div[4]/a""")
    click2.click()
    # wait 5 seconds for the downloading to complete
    # time.sleep(5)


test_download_from_chembl()
