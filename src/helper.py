from selenium.webdriver.common.by import By
from playsound import playsound
import time
from src import driver, STATIC


def login(usrnm, pswd):
    is_page_loaded = False
    while is_page_loaded == False:
        try:
            username = driver.find_element(By.ID, "login-input-email")
            pwd = driver.find_element(By.ID, "login-input-password")
            is_page_loaded = True
        except:pass
    # input login details and enter
    username.send_keys(usrnm)
    pwd.send_keys(pswd)
    driver.find_element(By.ID, "login-submit").click()

def loop_until_live(refresh_time):
    #def vars
    is_live = False
    login_successful = True
    #outer loop
    while is_live == False:
        is_page_loaded = False
        # check if page has finished loading
        while is_page_loaded == False:
            try:
                some_elem = driver.find_element(By.ID, "collaboration-element") #just a random html element, if found indicates page has loaded
                if login_successful == True:
                    playsound(f'{STATIC}/login.mp3')
                    login_successful = False
                is_page_loaded = True
            except:pass
        # check if session is live
        try:
            live_elem = driver.find_element(By.ID, "live-session-button-element")
            print('we are live')
            is_live = True
        except:
            time.sleep(refresh_time)
            driver.refresh() 