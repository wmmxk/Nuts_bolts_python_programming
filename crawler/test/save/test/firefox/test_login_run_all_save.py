'''
The hotkey for saving does not work
'''

import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains

from lib.save_notebook_firefox import save_notebook


def test_quant():
    """
    First login then go the notebooks page
    Then shutdown the previous open notebook; then delete.
    Open the next notebook; run it all and save the whole pages
    :return:
    """
    usr = "xkw2020@gmail.com"
    pwd = "xk123456"
    driver = webdriver.Firefox()
    driver.get("https://www.quantopian.com/signin")
    # log into the website
    username_box = driver.find_element_by_id("user_email")
    username_box.send_keys(usr)
    password_box = driver.find_element_by_id('user_password')
    password_box.send_keys(pwd)
    login_btn = driver.find_element_by_id('login-button')
    login_btn.click()
    driver.maximize_window()
    time.sleep(2)

    # hover over the "Research" menu and then click the "Notebooks" option
    print("double click")
    pyautogui.click(571, 0, clicks=2)
    # pyautogui.click(1363, 174)
    time.sleep(5)
    # pyautogui.click(1837, 451)
    # pyautogui.click(1837, 451)


    time.sleep(5)
    # deletion
    print("start deletion")
    pyautogui.click(1837, 451)
    pyautogui.click(1837, 451)
    time.sleep(5)
    # confirm deletion
    pyautogui.click(1328, 687)
    time.sleep(1)
    # driver.get("https://www.quantopian.com/research/notebooks/sanity_check.ipynb")

    print("end deletion")
    # open a notebook
    time.sleep(3)
    pyautogui.click(292, 454)
    time.sleep(10)
    # print("start saving-----")
    save_notebook(run_time=20)
    time.sleep(10)


test_quant()
