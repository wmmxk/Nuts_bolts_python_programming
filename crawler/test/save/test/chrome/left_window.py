'''
The hotkey for saving does not work
'''
#  the website is 175%
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
    # hover over the "Research" menu and then click the "Notebooks" option
    pyautogui.click(965, 144) # Research
    pyautogui.click(987, 330) # Notebooks
    time.sleep(1)
    # leave
    pyautogui.click(1161, 199)
    time.sleep(25)
    
    # deletion
    print("shutdown")
    pyautogui.click(1802, 571)
    time.sleep(12)
    print("click deetion")
    # start deletion
    pyautogui.click(1802, 571)
    time.sleep(1)
    # confirm deletion
    pyautogui.click(1489, 704)
    time.sleep(8) # make the next one pop up

    print("end deletion")
    # open a notebook
    pyautogui.click(394, 570)
    time.sleep(17)
    # Run
    pyautogui.click(1763, 218)
    time.sleep(1)
    pyautogui.click(1570, 417)
    time.sleep(165)

    # save
    pyautogui.click(1898, 80)
    time.sleep(0.2)
    pyautogui.click(1715, 371)
    time.sleep(0.2)
    pyautogui.click(1495, 374)
    time.sleep(0.2)
    # click save button
    pyautogui.click(1560, 104)
    time.sleep(3)
   



test_quant()
