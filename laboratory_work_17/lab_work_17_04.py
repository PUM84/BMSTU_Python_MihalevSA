import schedule
import time
from datetime import datetime

def task1():
    print(datetime.now().strftime('%H:%M:%S'), "- Задача 1 выполнена")

def task2():
    print(datetime.now().strftime('%H:%M:%S'), "- Задача 2 выполнена")

schedule.every(3).seconds.do(task1)
schedule.every(5).seconds.do(task2)

print("Планировщик запущен на 20 секунд")
print("Задача 1: каждые 3 секунды")
print("Задача 2: каждые 5 секунд")

start = time.time()
while time.time() - start < 20:
    schedule.run_pending()
    time.sleep(1)

schedule.clear()
print("Планировщик завершил работу")