
import time
import random
import requests
import json
from fake_useragent import UserAgent
#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

ua = UserAgent()
user_agent = ua.random

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user_agent}')
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def generic_password() -> str: #Password generation with 10 symbols
    password = ''
    for _ in range(11):
        password += random.choice(list('qwertyuiopasdfghjklzxcvbnm1234567890'))
    return password

def get_token(email: str, password: str) -> str: #Getting authorization token
    data = {"login": email, "password": password}

    headers = {
        'Content-type': 'application/json',
        'user-agent': user_agent
    }
    r = requests.post('https://discord.com/api/v9/auth/login', data=json.dumps(data), headers=headers)
    return r.json()['token']


def main() -> None: #main function
    try:
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
        driver.get('https://discord.com/register')
        wait = WebDriverWait(driver, 30)
        wait.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
        wait.until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys(nickname)
        wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/div/form/div/div/div[4]/div[1]/div[1]/div/div/div/div'))).click()
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(str(random.randint(1, 28))) 
        actions.send_keys(Keys.ENTER)
        actions.send_keys(str(random.randint(1, 12)))
        actions.send_keys(Keys.ENTER)
        actions.send_keys(str(random.randint(1970, 2004)))
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.button-1cRKG6'))).click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/div/section/div/div[2]'))).click()
        print('_'*50,'Press enter to continue', '_'*50, '\n')
        input()
    except Exception as error:
        print(error)
    finally:
        driver.quit()
    
if __name__ == '__main__':
    email = input('Введите email: ')
    nickname = input('Введите nickname: ')
    password = generic_password()
    main()
    print(get_token(email, password))
    print('_'*100)
    
    
    