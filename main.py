import sys
from selenium.webdriver.common.by import By
from playsound import playsound
from src.helper import login, loop_until_live
from src import driver, USERNAME, PASSWORD, REFRESH_EVERY, STATIC

#identify login text boxes and input login details
login(USERNAME, PASSWORD)
#loop until session is live
loop_until_live(REFRESH_EVERY)
#alert and enter session
driver.find_element(By.ID, "live-session-button-element").click()
playsound(f'{STATIC}/live.mp3')
#exit
sys.exit("Good luck in class today")