'''
The hotkey for saving does not work
'''

from lib.save_notebook import save_notebook
import pyautogui

import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui


def test_quant():
   """
   First login then go the notebooks page
   Then shutdown the previous open notebook; then delete.
   Open the next notebook; run it all and save the whole pages
   :return:
   """
   usr="xkw2020@gmail.com"
   pwd = "xk123456"
   driver = webdriver.Chrome(ChromeDriverManager().install()) # diver
   driver.get("https://www.quantopian.com/signin")
   # log into the website
   username_box = driver.find_element_by_id("user_email")
   username_box.send_keys(usr)
   password_box = driver.find_element_by_id('user_password')
   password_box.send_keys(pwd)
   login_btn = driver.find_element_by_id('login-button')
   login_btn.click()
   driver.maximize_window()
   time.sleep(3)


   # hover over the "Research" menu and then click the "Notebooks" option
   actions = ActionChains(driver)
   menu = driver.find_element_by_xpath("//*[@id='research-nav-header']")
   notebook_opt = driver.find_element_by_xpath("//*[@id='app-navbar-collapse']/ul/li[1]/ul/li[2]/a")
   actions.move_to_element(menu).move_to_element(notebook_opt).click().perform()

   time.sleep(5)
   # deletion
   print("start deletion")
   pyautogui.click(1835, 418)
   time.sleep(5)
   pyautogui.click(1835, 418)
   time.sleep(1)
   # confirm deletion
   pyautogui.click(1258, 676)
   # driver.get("https://www.quantopian.com/research/notebooks/sanity_check.ipynb")

   print("end deletion")
   # open a notebook
   time.sleep(3)
   pyautogui.click(237, 412)
   time.sleep(10)
   # print("start saving-----")
   save_notebook(run_time=20)
   time.sleep(10)

test_quant()
