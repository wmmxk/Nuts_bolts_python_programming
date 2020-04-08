import pyautogui
import time

def click_one_by_one(n=250):
    for i in range(n):
      pyautogui.click(1567, 574)
      time.sleep(2)
click_one_by_one()
