import random
import string
import os
import shutil
def write_names():
    with open("names.txt","a+",encoding="utf-8") as f:
        while True:
            name = input("请输入姓名(输入q退出):")
            if name == "q":
                break
            f.write(name + "\n")
        f.seek(0)
        print("文件中所有姓名:")
        print(f.read())

write_names()

with open("data.txt","w",encoding="utf-8") as f:
    for i in range(1,101):
        f.write(f"{i}\n")

def list_files_and_dirs(path="."):
    for item in os.listdir(path):
        print(item)

list_files_and_dirs()

def reverse_file_lines(filename):
    with open(filename,"r",encoding="utf-8") as f:
        lines = f.readlines()
    for line in reversed(lines):
        print(line,end="")

reverse_file_lines("exanple.txt")

def get_total_size(path="."):
    total = 0
    for dirpath,dirnames,filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath,f)
            total += os.path.getsize(fp)
    print(f"总大小:{total}字节")

get_total_size()

def find_files(keyword,path="."):
    for root, dirs, files in os.walk(path):
        for file in files:
            if keyword in file:
                rel_path = os.path.relpath(os.path.join(root,file))

find_files("test")

def create_random_pngs():
    for i in range(100):
        name = ''.join(random.choices(string.ascii_letters + string.digits,k=4))
        filename = f"img/{name}.png"
        with open(filename,"w") as f:
            pass

create_random_pngs()

def rename_images(suffix="_good",path="."):
    for file in os.listdir(path):
        if file.endswith((".png",".jpg",".jpeg")):
            name, ext = os.path.splitext(file)
            new_name=f"{name}{suffix}{ext}"
            os.rename(os.path.join(path,file),os.path.join(path,new_name))

rename_images()

def copy_directory(src,dst):
    shutil.copytree(src,dst)

copy_directory("source_dir","backup_dir")

def generate_ips(filename,count=1000):
    with open(filename,"w") as f:
        for _ in range(count):
            ip = f"210.34.59.{random.randint(1,255)}"
            f.write(ip + "\n")

def count_ips(filename):
    with open(filename,"r") as f:
        ips = f.read().splitlines()
        for ip,count in ips.most_common(10):
