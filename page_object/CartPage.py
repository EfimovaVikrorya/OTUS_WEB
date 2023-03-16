from config import time_sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        PAGE_NAME = "/apple/iphone"
        self.driver.get(self.driver.url + PAGE_NAME)

    def descrirtion(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#tab-description")))

    def add_to_cart(self):
        btn_cart = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
        btn_cart.click()

    def delete_from_cart(self):
        btn_cart = WebDriverWait(self.driver, time_sleep.NORM, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-danger")))
        btn_cart.click()

    def rating(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".rating")))
