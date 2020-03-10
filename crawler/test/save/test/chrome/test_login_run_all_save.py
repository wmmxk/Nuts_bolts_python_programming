'''
The hotkey for saving does not work
'''

import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
import sys
sys.path.insert(0, "../../")
from paths import chrome_driver_p
from lib.save_notebook import save_notebook


def test_quant():
    """
    First login then go the notebooks page
    Then shutdown the previous open notebook; then delete.
    Open the next notebook; run it all and save the whole pages
    :return:
    """
    usr = "xkw2020@gmail.com"
    pwd = "xk123456"
    driver = webdriver.Chrome(chrome_driver_p)  # diver
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
    time.sleep(13)
    pyautogui.click(1835, 418)
    time.sleep(3)
    # confirm deletion
    pyautogui.click(1258, 676)
    # driver.get("https://www.quantopian.com/research/notebooks/sanity_check.ipynb")

    print("end deletion")
    # open a notebook
    time.sleep(3)
    pyautogui.click(237, 412)
    time.sleep(8)
    # print("start saving-----")
    save_notebook(run_time=120, save_time=10)


test_quant()
