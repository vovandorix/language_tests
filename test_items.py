from selenium.webdriver.common.by import By
import time


def test_guest_should_see_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30) 
    browser.implicitly_wait(5)
    input1=browser.find_elements(By.CSS_SELECTOR, '.add-to-basket>button')
    assert input1, 'item not found!'
