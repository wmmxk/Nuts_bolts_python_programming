```
source: https://stackoverflow.com/questions/53729201/save-complete-web-page-incl-css-images-using-python-selenium
```

import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui

URL = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastx&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'
SEQUENCE = 'CCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACA' #'GAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGAGAAGA'

# open page with selenium
# (first need to download Chrome webdriver, or a firefox webdriver, etc)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)

# enter sequence into the query field and hit 'blast' button to search
seq_query_field = driver.find_element_by_id("seq")
seq_query_field.send_keys(SEQUENCE)

blast_button = driver.find_element_by_id("b1")
blast_button.click()

# wait until results are loaded
# WebDriverWait(driver, 120).until(visibility_of_element_located((By.ID, 'grView')))

time.sleep(60)
# open 'Save as...' to save html and assets

pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.typewrite(SEQUENCE + '.html')
pyautogui.hotkey('enter')
