from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import ahk

firefox = FirefoxBinary("/usr/bin/firefox")
from selenium import webdriver

driver = web.Firefox(firefox_binary=firefox)
driver.get("http://www.yahoo.com")
ahk.start()
ahk.ready()
ahk.execute("Send,^s")
ahk.execute("WinWaitActive, Save As,,2")
ahk.execute("WinActivate, Save As")
ahk.execute("Send, C:\\path\\to\\file.htm")
ahk.execute("Send, {Enter}")
