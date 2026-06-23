import shutil
import os
from datetime import datetime

def create_backup(source, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir + "/backup_" + timestamp
    os.makedirs(backup_dir, exist_ok=True)
    shutil.copytree(source, backup_path)
    print("Резервная копия создана:", backup_path)

def restore_backup(backup_path, target):
    if os.path.exists(target):
        shutil.rmtree(target)
    shutil.copytree(backup_path, target)
    print("Восстановление выполнено:", backup_path, "->", target)

def change_permissions(path, mode):
    os.chmod(path, mode)
    print("Права доступа изменены на", oct(mode))

def print_permissions(path):
    stat = os.stat(path)
    print("Права доступа:", oct(stat.st_mode)[-3:])

os.makedirs("data", exist_ok=True)
with open("data/file1.txt", "w") as f:
    f.write("Тестовый файл 1")
with open("data/file2.txt", "w") as f:
    f.write("Тестовый файл 2")

with open("test_permissions.txt", "w") as f:
    f.write("Файл для прав доступа")

create_backup("data", "backups")

print_permissions("test_permissions.txt")
change_permissions("test_permissions.txt", 0o755)
print_permissions("test_permissions.txt")
change_permissions("test_permissions.txt", 0o644)
print_permissions("test_permissions.txt")

shutil.rmtree("data")
shutil.rmtree("backups")
os.remove("test_permissions.txt")