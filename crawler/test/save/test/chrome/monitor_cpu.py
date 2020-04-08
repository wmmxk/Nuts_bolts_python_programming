import psutil
import time

def monitor_chrome():
   chrome_usage = []
   for p in psutil.process_iter():
      if p.name() == "chrome":
          chrome_usage.append(p.cpu_percent())
   res = sorted(chrome_usage, reverse=True)
   return sum(res[:2])
   


    
def monitor_every_second(interval=0.2):
      time.sleep(interval)
      return monitor_chrome()


while True:
    print(monitor_every_second(0.2))
