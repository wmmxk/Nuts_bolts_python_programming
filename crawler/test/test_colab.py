"""
source: https://www.youtube.com/watch?v=Hw21qZs7xkA
"""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from getpass import getpass
import time
from selenium.webdriver import ActionChains


def test_facebook_log():
    driver = webdriver.Chrome(ChromeDriverManager().install()) # diver
    driver.get("https://colab.research.google.com/notebooks/intro.ipynb")

    driver.maximize_window()
    time.sleep(3)
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    menu = driver.find_element_by_xpath("//*[@id='runtime-menu-button']/div/div/div[1]")
    run_button = driver.find_element_by_xpath("//*[@id=':1p']/div")
    actions = actions.move_to_element(menu).click()
    time.sleep(4)
    actions.move_to_element(run_button).click().perform()
    print("to click")
    time.sleep(50)

test_facebook_log()
