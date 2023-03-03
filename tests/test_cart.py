from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PAGE_NAME = "/apple/iphone"


class Config:
    FAST = 1
    NORM = 2
    SLOW = 3
    VERY_SLOW = 4


def test_cart_text_description(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#tab-description")))
    assert el.text == 'iPhone is a revolutionary new mobile phone that allows you to make a call by ' \
                      'simply tapping a name or number in your address book, a favorites list, or a ' \
                      'call log. It also automatically syncs all your contacts from a PC, Mac, or ' \
                      'Internet service. And it lets you select and listen to voicemail messages in ' \
                      'whatever order you want just like email.'


def test_cart_alert_success(driver):
    driver.get(driver.url + PAGE_NAME)
    btn_cart = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    btn_cart.click()
    alert = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
    assert alert.text == "Success: You have added iPhone to your shopping cart!\n×"


def test_cart_item_in_sopping_cart(driver):
    driver.get(driver.url + PAGE_NAME)
    btn_cart = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    btn_cart.click()
    time.sleep(10)
    btn_item = WebDriverWait(driver, Config.NORM, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart-total")))
    assert btn_item.text == '1 item(s) - $123.20'


def test_cart_item_reset(driver):
    driver.get(driver.url + PAGE_NAME)
    btn_cart = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    btn_cart.click()
    time.sleep(10)
    btn_item = WebDriverWait(driver, Config.NORM, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart-total")))
    assert btn_item.text == '1 item(s) - $123.20'
    btn_item.click()
    btn_danger = WebDriverWait(driver, Config.NORM, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-danger")))
    btn_danger.click()
    time.sleep(10)
    btn_item = WebDriverWait(driver, Config.NORM, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart-total")))
    assert btn_item.text == '0 item(s) - $0.00'


def test_cart_rating(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".rating")))
    assert el.text == '0 reviews / Write a review\nTweet\nShare'
