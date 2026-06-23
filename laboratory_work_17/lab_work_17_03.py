import psutil
import time

def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_memory():
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk():
    disk = psutil.disk_usage('/')
    return disk.percent

def list_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        print("PID:", proc.info['pid'], "Имя:", proc.info['name'])

print("Информация о системе:")
print("CPU ядер:", psutil.cpu_count())
mem = psutil.virtual_memory()
print("Память всего:", mem.total // (1024**2), "МБ")
disk = psutil.disk_usage('/')
print("Диск всего:", disk.total // (1024**3), "ГБ")

print("\nТоп процессов:")
list_processes()

print("\nМониторинг ресурсов (10 секунд):")
start = time.time()
while time.time() - start < 10:
    cpu = get_cpu()
    mem_percent = get_memory()
    disk_percent = get_disk()
    print("CPU:", cpu, "%", "Память:", mem_percent, "%", "Диск:", disk_percent, "%")
    time.sleep(2)