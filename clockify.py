from selenium import webdriver
from seleniumwire import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


browser = webdriver.Chrome()
browser.set_window_position(0, 0)
browser.set_window_size(1920, 1080)
browser.implicitly_wait(10)
link = "https://clockify.me"


def check_element():
        try:
            browser.find_element(By.CSS_SELECTOR, "div.toast-title")
        except NoSuchElementException:
            return False
        return True


def compareName():
        if oldName != newName:
            print("Имя изменилось, тест пройден")
        else:
            print("Имя не изменилось, тест провален")

nameList = ["Катя", "Петя", "Владимир", "Колян", "Алексей", "Арсений", "Яна"]
newName = random.choice(nameList)

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".header__row__item_right li").click()
    browser.find_element(By.ID, "email").send_keys("whcxobdriqi@tmp-mail.ru")
    browser.find_element(By.ID, "password").send_keys("Simple123456")
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    time.sleep(5)
    lk = browser.find_element(By.CSS_SELECTOR, ".cl-no-image-wrapper-sm")
    lk.click()
    browser.find_element(By.LINK_TEXT, "Profile settings").click()
    inputName = browser.find_element(By.CSS_SELECTOR, "input[data-cy=profile-name]")
    oldName = inputName.get_attribute("value")
    inputName.clear()
    if oldName == newName:
        newName = random.choice(nameList)
        inputName.send_keys(newName)
        browser.find_element(By.TAG_NAME, "body").click()
    else:
        inputName.send_keys(newName)
        browser.find_element(By.TAG_NAME, "body").click()
    
     
    check_element()
    status = browser.requests[-1].response.status_code
    
finally:
    compareName()
    if check_element() == True:
        print('Сообщение "Settings successfully saved" появилось. Тест пройден')
    else:
        print('Сообщение "Settings successfully saved" не появилось. Тест не пройден')

    if status == 200:
        print("Status code", status, "Тест пройден")
    else:
        print("Status code", status, "Тест не пройден")
    time.sleep(5)
    browser.quit()
