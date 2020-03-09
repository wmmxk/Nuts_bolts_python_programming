"""
source: https://www.youtube.com/watch?v=Hw21qZs7xkA
"""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains


def test_click_button_log():
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
    time.sleep(3)

    # try to open the "sanity_check.ipynb" notebook by clicking it    
    actions = ActionChains(driver)
    notebook_button = driver.find_element_by_xpath("//*[@id='notebook_list']/div[2]/div/a/span")
    actions.move_to_element(notebook_button).click().perform()
    time.sleep(200)

test_click_button_log()
