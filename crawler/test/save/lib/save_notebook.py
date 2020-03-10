
import pyautogui
import time


def save_notebook(run_time=12, save_time=6):

    # run all
    pyautogui.click(1843, 217)
    pyautogui.click(1731, 324)
    time.sleep(run_time)
    print("Save file")

    # more tools
    pyautogui.click(1897, 78)
    pyautogui.click(1669, 373)
    pyautogui.click(1469, 373)
    # you have to click twice
    # save button
    pyautogui.click(1559, 105)
    pyautogui.click(1559, 105)
    time.sleep(save_time)
    # cancel Leave site
