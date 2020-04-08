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

# 150%
def test_quant():
    """
    First login then go the notebooks page
    Then shutdown the previous open notebook; then delete.
    Open the next notebook; run it all and save the whole pages
    :return:
    """
    # hover over the "Research" menu and then click the "Notebooks" option
    pyautogui.click(3029, 147) # Research
    pyautogui.click(3055, 305) # Notebooks
    time.sleep(3)
    # leave
    pyautogui.click(3044, 170)
    time.sleep(10)
    
    # deletion
    print("shutdown")
    pyautogui.click(3739, 515)
    time.sleep(15)
    # start deletion
    pyautogui.click(3739, 515)
    time.sleep(3)
    # confirm deletion
    pyautogui.click(3288, 693)
    time.sleep(8) # make the next one pop up

    print("end deletion")
    # open a notebook
    pyautogui.click(2168, 515)
    time.sleep(15)
    # Run
    pyautogui.click(3701, 208)
    time.sleep(1)
    pyautogui.click(3544, 376)
    time.sleep(110)

   # save
    pyautogui.click(3824, 52)
    time.sleep(1.1)
    pyautogui.click(3588, 341)
    time.sleep(1)
    pyautogui.click(3488, 341)
    time.sleep(1.2)
    # click save button
    pyautogui.click(3450, 93)
    time.sleep(7.3)
   



test_quant()
