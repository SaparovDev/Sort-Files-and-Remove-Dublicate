'''Python File di jiynaw ham dublikatin oshiriw'''

from pathlib import Path
import shutil
import os


'''Userden juwap aliw ushin'''
sorawshi = input("File lardi jiynap dublikatlarin oshiriw [awa/yaq]:  ")

# Funkcyalar

def file_sort():
    '''File lardi bir papkag'a jiynaydi'''
    Path("Python_Files").mkdir(exist_ok=True)
    for file in Path(".").glob("*.py"): 
        shutil.copy(file, "Python_Files")


def dublicate_remove():
    '''Dublicat file lardi oshiredi'''
    for file in Path(".").glob("*.py"):
        if file.name != "main.py":
            file.unlink()
    

'''Shart operatorlari'''

if sorawshi == "awa":
    file_sort()
    dublicate_remove()
    print("Sizin file lariniz Python_Files atli papkag'a koshirildi")

elif sorawshi == "yaq":
    print("Process juwmaqlandi")
    exit()

else:
    print("Juwapti qayta kirgiz")