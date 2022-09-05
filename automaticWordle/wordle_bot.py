from enum import Flag
from pip import main
from pyautogui import write, press, leftClick, screenshot, locateAllOnScreen, FAILSAFE, PAUSE, pixel, pixelMatchesColor, typewrite
from time import sleep
from random import randint

def main():
    # When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program:
    FAILSAFE = True

    wrong_letter = tuple((120, 124, 126))
    correct_letter = tuple((106, 170, 100))
    misplaced_letter = tuple((201, 180, 88))

    # guesses = 0
    # these two guesses should reduce the word list drastically 
    first_guess = 'scale'
    second_guess = 'group'
    # third-sixth will be replaced 
    third_guess = 'loser'
    fourth_guess = 'quest'
    fifth_guess = 'sorry'
    sixth_guess = 'midge'
    # import a list of 5 letter words, there's no check on the words, so they need to be 5 letters long
    word_list = import_word_list('all_words.txt')
    # letters that wordle marks grey will be added here
    not_in_word = set()
    # this list contains the letters that get marked yellow for a given position
    not_in_position = [set(), set(), set(), set(), set()]
    # These are the green marked letters, though idk why I didn't just make this a str...
    correct_letters = ['0', '0', '0', '0', '0']
    # lazily corrected method for removing letters if they are marked grey
    def check_words(words: list) -> list:
        better_words = []
        somewhere = ''
        for positions in not_in_position:
            somewhere += str(positions)
        for word in words:
            bad = False
            for letter in not_in_word:
                if letter in word and letter not in correct_letters and letter not in somewhere:
                    bad = True
            if not bad:
                better_words.append(word)
        not_in_word.clear()
        return better_words
    # removes words that have a yellow letter in the position they were marked yellow in
    def check_letter_positions(words: list, not_in_position: set) -> list:
        better_words = []
        for word in words:
            bad = False
            for position in not_in_position:
                if word[not_in_position.index(position)] in position:
                    bad = True
                for letter in position:
                        if letter not in word:
                            bad = True
            if not bad:
                better_words.append(word)
        not_in_position = [set(), set(), set(), set(), set()]
        return better_words
    # removes words from the list that do not have a letter marked green in the marked position
    def check_correct_positions(words: list, correct_letters: list) -> list:
        better_words = []
        for word in words:
            bad = False
            for idx, letter in enumerate(correct_letters):
                if letter != '0':
                    if word[idx] != letter:
                        bad = True
            if not bad:
                better_words.append(word)
        return better_words

    open_wordle_in_incognito()

    sleep(2)

    letter_boxes = get_letter_locations()

    print(len(word_list))

    make_guess(first_guess)

    def Check_Correct_Letters(guess):
        is_valid = True
        for position in range(0, 5):
            left = letter_boxes[position][0]
            top = letter_boxes[position][1]
            if (pixel(int(left), int(top)) == wrong_letter):
                not_in_word.add(guess[position])
            elif (pixel(int(left), int(top)) == misplaced_letter):
                not_in_position[position].add(guess[position])
            elif (pixel(int(left), int(top)) == correct_letter):
                correct_letters[position] = guess[position]
            else:
                press('backspace', presses=5)
                is_valid = False
        if is_valid:
            del letter_boxes[0:5]

    Check_Correct_Letters(first_guess)

    # update wordlist based on letters not in the word.
    # not sure the best way to do this quickly. checking every word with every letter will be pretty slow.
    word_list = check_words(word_list)

    word_list = check_letter_positions(word_list, not_in_position)

    word_list = check_correct_positions(word_list, correct_letters)
    print(f"Possible words after 1 guess: {len(word_list)}")

    #if len(word_list) > 0:
    #    second_guess = word_list[randint(0,(len(word_list) - 1))]
    
    make_guess(second_guess)

    Check_Correct_Letters(second_guess)

    word_list = check_words(word_list)
    word_list = check_letter_positions(word_list, not_in_position)
    word_list = check_correct_positions(word_list, correct_letters)

    print(f"Possible words after 2 guesses: {len(word_list)}")

    if len(word_list) > 0:
        third_guess = word_list[randint(0,(len(word_list) - 1))]

    make_guess(third_guess)

    Check_Correct_Letters(third_guess)

    word_list = check_words(word_list)
    word_list = check_letter_positions(word_list, not_in_position)
    word_list = check_correct_positions(word_list, correct_letters)

    print(f"Possible words after 3 guesses: {len(word_list)}")

    if len(word_list) > 0:
        forth_guess = word_list[randint(0,(len(word_list) - 1))]
    
    make_guess(forth_guess)

    Check_Correct_Letters(forth_guess)

    word_list = check_words(word_list)
    word_list = check_letter_positions(word_list, not_in_position)
    word_list = check_correct_positions(word_list, correct_letters)

    print(f"Possible words after 4 guesses: {len(word_list)}")

    if len(word_list) > 0:
        fifth_guess = word_list[randint(0,(len(word_list) - 1))]
    
    make_guess(fifth_guess)

    print(f"Possible words after 5 guesses: {len(word_list)}, fingers = crossed")

    word_list = check_words(word_list)
    word_list = check_letter_positions(word_list, not_in_position)
    word_list = check_correct_positions(word_list, correct_letters)

    if len(word_list) > 0:
        sixth_guess = word_list[randint(0,(len(word_list) - 1))]

    make_guess(sixth_guess)
    print(f"Possible words after 2 guesses: {len(word_list)}, close?")

def make_guess(word_guess):
    typewrite(word_guess, 0.1)

    sleep(1)

    press('enter')

    sleep(3)

def import_word_list(words_file: str) -> list:
    with open(words_file) as text:
        words = text.read()
        stripped = words.strip('[]')
        replaced = stripped.replace("'","")
        word_list = replaced.split(', ')
        return(word_list)

def get_letter_locations() -> list:
    letter_boxes = [((location.left + 7 ), (location.top + 7)) for location in locateAllOnScreen('letter_box.png')]
    return letter_boxes
# pyautogui commands to open chrome in incognito and navigate to wordle as well as click on the screen to close the tutorial popup
def open_wordle_in_incognito():
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

if __name__ == '__main__':
    main()
