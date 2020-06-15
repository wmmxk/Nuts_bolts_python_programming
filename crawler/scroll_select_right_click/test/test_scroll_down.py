import pyautogui
import time


def test_scroll():
    w, h = pyautogui.size()
    print("width and height", w, h)
    print("The current position of mouse")
    print(pyautogui.position())
    pyautogui.moveRel(-1000, 0, duration=0.05)
    last_100_trades_coor = (3021, 751)
    pyautogui.click(last_100_trades_coor[0], last_100_trades_coor[1])

    time.sleep(3)
    time_slots_coor = (3021, 898) # 683, 730, 777,822
    pyautogui.click(time_slots_coor[0], time_slots_coor[1])
    time.sleep(3)
    pyautogui.scroll(-500)
    pass
