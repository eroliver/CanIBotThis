from pyautogui import write, press, leftClick, screenshot, locateAllOnScreen, FAILSAFE, PAUSE, pixel, pixelMatchesColor, typewrite
from time import sleep
from random import randint


# https://github.com/madalynrose/Words/blob/master/assets/5-letter.txt is where the word list came from.
# Colors for checking if letters are correct
# not in word = 120, 124, 126
# in wrong location = 201, 180, 88
# correct letter, correct spot = 106, 170, 100

PAUSE = 3
FAILSAFE = True

wrong_letter = tuple((120, 124, 126))
correct_letter = tuple((106, 170, 100))
misplaced_letter = tuple((201, 180, 88))

#guesses = 0

first_guess = 'years'
second_guess = 'timed'
third_guess = 'group'
fourth_guess = 'quest'

def import_word_list():
    with open('word_list.txt') as text:
        words = text.read()
        stripped = words.strip('[]')
        replaced = stripped.replace("'","")
        word_list = replaced.split(', ')
        return(word_list)

word_list = import_word_list()

not_in_word = set()
not_in_position = [set(), set(), set(), set(), set()]

third_guess = word_list[randint(0,1000)]

press('win')

sleep(2)

write('"C:\Program Files\Google\Chrome\Application\chrome.exe" -incognito')

sleep(2)

press('enter')

sleep(3)

write('https://www.nytimes.com/games/wordle/index.html')

press('enter')

sleep(3)

leftClick(500, 500)

sleep(5)

letter_boxes = []

letter_boxes = [((location.left + 7 ), (location.top + 7)) for location in locateAllOnScreen('letter_box.png')]

typewrite(first_guess, 0.1)

sleep(1)

press('enter')

sleep(3)

def Check_Correct_Letters(guesses, guess):
    for position in range(0, 5):
        left = letter_boxes[position][0]
        top = letter_boxes[position][1]
        if (pixel(int(left), int(top)) == wrong_letter):
            not_in_word.add(guess[position])
        elif (pixel(int(left), int(top)) == misplaced_letter):
            not_in_position[position].add(guess[position])
    del letter_boxes[0:5]


# for coordinate in letter_boxes:
#     left = coordinate[0]
#     top = coordinate[1]
#     print((pixel(int(left), int(top))))

#press('enter')

Check_Correct_Letters(0, first_guess)

# update wordlist based on letters not in the word.
# not sure the best way to do this quickly. checking every word with every letter will be pretty slow.
updated_list = []
for word in word_list:
    pass

sleep(3)

typewrite(second_guess, 0.1)

sleep(1)

press('enter')

sleep(3)

Check_Correct_Letters(1, second_guess)

sleep(3)

typewrite(third_guess, 0.1)

sleep(1)

press('enter')

sleep(3)

Check_Correct_Letters(1, third_guess)

print(not_in_word)
print(not_in_position)
