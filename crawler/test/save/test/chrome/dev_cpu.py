import psutil
import time

chrome_usage = []
for p in psutil.process_iter():
   if p.name() == "chrome":
       chrome_usage.append(p.cpu_percent())

print(sum(chrome_usage))
