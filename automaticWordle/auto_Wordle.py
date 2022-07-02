from time import sleep
from cv2 import solveP3P
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.timeouts import Timeouts

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.nytimes.com/games/wordle/index.html")
#assert "Python" in driver.title
wordleGame = driver.find_element(By.ID, 'wordle-app-game')
sleep(2)
wordleGame.click()
sleep(2)
#keyboard = driver.find_element(By.ID, "Keyboard-module_keyboard_1HSnn")
#keyboardElement = wordleGame.find_element(By.XPATH, "//*[contains(@class,'Board-module_board')]")
#keyboardElement.send_keys("abc")
wordleGame.send_keys("absd")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
sleep(5)

driver.close()