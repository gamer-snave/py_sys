
#! python3
WTF="""
██╗    ██╗████████╗███████╗██╗██╗
██║    ██║╚══██╔══╝██╔════╝██║██║
██║ █╗ ██║   ██║   █████╗  ██║██║
██║███╗██║   ██║   ██╔══╝  ╚═╝╚═╝
╚███╔███╔╝   ██║   ██║     ██╗██╗
 ╚══╝╚══╝    ╚═╝   ╚═╝     ╚═╝╚═╝
"""
#importing colorama for coloring output
import colorama
from colorama import Fore 
import time  # Buying time to sleep
import sys,os
colorama.init(autoreset=True)
print(Fore.RED+WTF)
print(Fore.GREEN+"Am closing all programs for you and restart this stupid computer!")
loading=['*','*','*','*']
for i in loading:
    time.sleep(1)
    print(i)
os.system("shutdown /r")
    
