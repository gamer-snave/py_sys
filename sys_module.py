import sys
import os
import time
import colorama 
from colorama import Back, Fore,Style
colorama.init(autoreset=True) #initializing colorama
print(Fore.YELLOW+"Stupid Codes Series!")
time.sleep(1.0)
print(Fore.GREEN+"pLAyiNG with Python Sys Module!")
# This is a simple program to display codding  Environment varibles
os.system("echo 'Python Version: ")
pythonv=os.system("python --version ")
print(Fore.YELLOW+str(pythonv))
modules=sys.builtin_module_names
version=sys.version
path=sys.executable

print("Python Excecutable file location:"+Fore.GREEN+str(path))
print("System Version: "+Fore.GREEN+str(version))

# sys.exec_prefix  shows path prefix
print("Default Encoding is:" + Fore.GREEN+str(sys.getdefaultencoding()))

print("System version"+ version)
os.system("echo 'Python Built In Modules: ")
def display_modules():
    for i in modules:
        print(Fore.CYAN+i)
        time.sleep(0.1)
display_modules()
time.sleep(5)
os.system('cls')
print(Fore.RED+"goodbye!!")

