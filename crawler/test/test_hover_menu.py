"""
You tried the tutorial in this video:https://www.youtube.com/watch?v=HYS3M_TOuFE  on the website of Nike
"""

import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Drpdowm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) # diver
    def test_drpdown(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://www.nike.com") 
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        men_menu = driver.find_element_by_xpath("//*[@id='gen-nav-commerce-header']/header/nav[1]/section[2]/div/div[2]/ul/li[2]/a")
        shoe_menu = driver.find_element_by_xpath("//*[@id='NavigationMenu-1']/div/div[2]/a[1]")
        #men_menu = driver.find_element_by_css_selector("li[data-nav-tracking=men]")
        tenis_option = driver.find_element_by_xpath("//*[@id='NavigationMenu-1']/div/div[2]/a[11]")
        actions.move_to_element(men_menu).move_to_element(shoe_menu).move_to_element(tenis_option).click().perform()
        
        # click shirt
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li[data-nav-tracking=men] a[data-subnav-label$=Shirts]"))).click()
 
    def tearDown(self):
        time.sleep(200)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
