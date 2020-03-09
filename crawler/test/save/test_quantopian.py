
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui

def test_quant():
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
   print("start saving-----")   
   pyautogui.hotkey('ctrl', 's')
   time.sleep(5)
   pyautogui.typewrite('quant.html')
   pyautogui.hotkey('enter')
   time.sleep(20)
test_quant()
