from pyautogui import write, press, leftClick, screenshot
from time import sleep

press('win')

sleep(2)

write('chrome')

sleep(2)

press('enter')

sleep(3)

write('https://www.nytimes.com/games/wordle/index.html')

press('enter')

sleep(3)

leftClick(500, 500)

write('years')

press('enter')


sleep(3)

screen = screenshot()
screen.save('first_guess.png')

