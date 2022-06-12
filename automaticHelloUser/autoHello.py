from random import random
from pyautogui import write, press, keyDown, keyUp, hotkey
from os import getcwd, path
from time import sleep
from random import randint
from config import *

path = getcwd()
bashPath = path.replace("\\", "/")
botName = botNames[(randint(0,(len(botNames) - 1)))]

def goToFolder():
    hotkey('win', 'e')
    hotkey('alt', 'd')
    write(path, interval=0.01)
    press('enter')

def openBashHere():
    hotkey('shift', 'f10')
    press('s')
    press('enter')

def echoOverwrite(text: str):
    write(f"echo {text} > botHello.py", interval=0.02)
    press('enter')

goToFolder()
openBashHere()
echoOverwrite("")

write(f'code {helloFileName}', interval=0.02)
press('enter')

sleep(3)

write('name = input("What is your name? ")\n')
write('print(f"Hello, {name}")\n')

sleep(3)

hotkey('ctrl', 's')

sleep(1)

goToFolder()
openBashHere()

sleep(1)

write(f'py {helloFileName}')

press('enter')

sleep(1)

write(f'{ botName }', interval=0.5)

press('enter')
