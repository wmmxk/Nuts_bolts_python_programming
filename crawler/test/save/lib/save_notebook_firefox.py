
import pyautogui
import time


def save_notebook(run_time=12, save_time=6):

    # run all
    pyautogui.click(1822, 214)
    pyautogui.click(1703, 352)
    time.sleep(run_time)
    print("Save file")

    # more tools
    pyautogui.click(1903, 109)
    pyautogui.click(1698, 548)

    # you have to click twice
    # save button
    pyautogui.click(1555, 104)

    # cancel Leave site
