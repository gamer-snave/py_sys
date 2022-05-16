import time
import os
import colorama
from colorama import Fore, Back
import sys

colorama.init(autoreset=True)

hbd='''
╔╗ ╔╗                      ╔══╗       ╔╗ ╔╗    ╔╗              ╔═══╗╔╗          ╔╗
║║ ║║                      ║╔╗║      ╔╝╚╗║║    ║║              ║╔═╗║║║          ║║
║╚═╝║╔══╗ ╔══╗╔══╗╔╗ ╔╗    ║╚╝╚╗╔╗╔═╗╚╗╔╝║╚═╗╔═╝║╔══╗ ╔╗ ╔╗    ║╚══╗║╚═╗╔══╗╔══╗║║
║╔═╗║╚ ╗║ ║╔╗║║╔╗║║║ ║║    ║╔═╗║╠╣║╔╝ ║║ ║╔╗║║╔╗║╚ ╗║ ║║ ║║    ╚══╗║║╔╗║║╔╗║║╔╗║╚╝
║║ ║║║╚╝╚╗║╚╝║║╚╝║║╚═╝║    ║╚═╝║║║║║  ║╚╗║║║║║╚╝║║╚╝╚╗║╚═╝║    ║╚═╝║║║║║║║═╣║║═╣╔╗
╚╝ ╚╝╚═══╝║╔═╝║╔═╝╚═╗╔╝    ╚═══╝╚╝╚╝  ╚═╝╚╝╚╝╚══╝╚═══╝╚═╗╔╝    ╚═══╝╚╝╚╝╚══╝╚══╝╚╝
          ║║  ║║  ╔═╝║                                ╔═╝║                        
          ╚╝  ╚╝  ╚══╝                                ╚══╝                        
'''


hi= '''                                   
▀████▀  ▀████▀▀███▀▀▀██▄███▀▀▀██▄  
  ██      ██    ██    ██ ██    ▀██▄
  ██      ██    ██    ██ ██     ▀██
  ██████████    ██▀▀▀█▄▄ ██      ██
  ██      ██    ██    ▀█ ██     ▄██
  ██      ██    ██    ▄█ ██    ▄██▀
▄████▄  ▄████▄▄████████▄████████▀  
                                   
                                   
'''




From ='''
█▀▀ █▀█ █▀█ █▀▄▀█ ▀
█▀░ █▀▄ █▄█ █░▀░█ ▄  \n
                                           
 ▄█▀▀▀█▄█                                      
▄██    ▀█                                      
▀███▄   ▀████████▄  ▄█▀██▄ ▀██▀   ▀██▀  ▄▄█▀██ 
  ▀█████▄ ██    ██ ██   ██   ██   ▄█   ▄█▀   ██
▄     ▀██ ██    ██  ▄█████    ██ ▄█    ██▀▀▀▀▀▀
██     ██ ██    ██ ██   ██     ███     ██▄    ▄
█▀█████▀▄████  ████▄████▀██▄    █       ▀█████▀
                                               
                                               
'''

def display(message):
    for char in message:
      
        sys.stdout.write(Fore.GREEN+Back.BLACK+char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.00005)
        else:
            time.sleep(0.005)
    
def blue_display(message):
    for char in message:
       
        sys.stdout.write(Fore.BLUE+Back.BLACK+char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.00005)
        else:
            time.sleep(0.005)
def yellow_display(message):
    for char in message:
        sys.stdout.write(Fore.YELLOW+Back.BLACK+char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.00005)
        else:
            time.sleep(0.005)

os.system('cls')
blue_display(hi)
display(hbd)
os.system('cls')
yellow_display(From)

