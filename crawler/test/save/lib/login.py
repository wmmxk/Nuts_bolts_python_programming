import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def login_quant():
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
    return driver
