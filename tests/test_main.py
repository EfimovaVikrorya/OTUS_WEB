from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PAGE_NAME = "/index.php"


class Config:
    FAST = 1
    NORM = 2
    SLOW = 3
    VERY_SLOW = 4


def test_main_currency(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".hidden-md")))
    assert el.text == "Currency"


def test_main_logo(driver):
    driver.get(driver.url + PAGE_NAME)
    WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))


def test_main_wishlist(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-shopping-cart")))
    el.click()
    el1 = WebDriverWait(driver, Config.VERY_SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-sm-12")))
    assert el1.text == "Shopping Cart\nYour shopping cart is empty!\nContinue"


def test_main_search(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#search")))
    assert el.text == ""


def test_main_acccount(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".fa-phone")))
    el.click()
    el = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content")))
    assert el.text == ('Contact Us\n'
                        'Our Location\n'
                        'Your Store\n'
                        'Address 1\n'
                        'Telephone\n'
                        '123456789\n'
                        '\n'
                        'Contact Form\n'
                        'Your Name\n'
                        'E-Mail Address\n'
                        'Enquiry')

