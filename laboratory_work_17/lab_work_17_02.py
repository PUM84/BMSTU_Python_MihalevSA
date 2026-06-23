import shutil
import os

def copy_file(src, dst):
    shutil.copy(src, dst)
    print("Файл", src, "скопирован в", dst)

def copy_directory(src, dst):
    shutil.copytree(src, dst)
    print("Директория", src, "скопирована в", dst)

def delete_file(filename):
    os.remove(filename)
    print("Файл", filename, "удален.")

def delete_directory(dirname):
    shutil.rmtree(dirname)
    print("Директория", dirname, "удалена.")

with open("source.txt", "w") as f:
    f.write("Текст копируемого файла.")

os.makedirs("test_dir", exist_ok=True)
with open("test_dir/test.txt", "w") as f:
    f.write("Вложенный файл")

copy_file("source.txt", "destination.txt")
copy_directory("test_dir", "test_dir_copy")
delete_file("destination.txt")
delete_directory("test_dir_copy")