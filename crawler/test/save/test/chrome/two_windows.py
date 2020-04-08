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
    time.sleep(0.5)
    # leave
    pyautogui.click(1161, 199)

    # right window
    pyautogui.click(3029, 147) # Research
    pyautogui.click(3055, 305) # Notebooks
    time.sleep(0.5)
    # leave
    pyautogui.click(3044, 170)
    time.sleep(40)

    
    # left shutdown
    print("shutdown")
    pyautogui.click(1802, 571)
    # right shutdown
    print("shutdown")
    pyautogui.click(3739, 515)
    time.sleep(16)

    # left deletion
    pyautogui.click(1803, 571)
    # right deletion
    pyautogui.click(3739, 515)
    time.sleep(1)
    # confirm left deletion
    pyautogui.click(1455, 683)
    # confirm right deletion
    pyautogui.click(3288, 693)
    time.sleep(12) # make sure the next one pop up

    # open left notebook
    pyautogui.click(394, 570)
    # open right notebook
    pyautogui.click(2168, 515)
    time.sleep(15)
    
    # left Run
    pyautogui.click(1763, 218)
    time.sleep(1)
    pyautogui.click(1570, 417)
    time.sleep(2)
    # right run
    pyautogui.click(3701, 208)
    time.sleep(1)
    pyautogui.click(3544, 376)
    time.sleep(132)

    # left save
    pyautogui.click(1898, 80)
    time.sleep(0.1)
    pyautogui.click(1715, 371)
    time.sleep(0.1)
    pyautogui.click(1495, 374)
    time.sleep(0.1)
    # click save button
    pyautogui.click(1560, 104)
    time.sleep(0.1)
   
    # right_save
    pyautogui.click(3824, 52)
    time.sleep(0.1)
    pyautogui.click(3588, 341)
    time.sleep(0.1)
    pyautogui.click(3488, 341)
    time.sleep(0.1)
    # click save button
    pyautogui.click(3450, 93)
    time.sleep(5)




test_quant()
