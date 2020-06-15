import pyautogui
import time


def test_dragging():
    time.sleep(1)
    pyautogui.click()  # click to put drawing program in focus
    distance = 400
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2)  # move down
        pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=0.2)  # move up


def test_dragging_select():
    pyautogui.click()
    pyautogui.dragRel(500, 500)
    pyautogui.scroll(-100)
    pyautogui.dragRel(500, 500)
