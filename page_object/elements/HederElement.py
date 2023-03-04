from config import time_sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HederElement:
    def __init__(self, driver):
        self.driver = driver

    def logo(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-brand")))

    def items_in_cart(self):
        return WebDriverWait(self.driver, time_sleep.NORM, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart-total")))

    def currency(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Currency']")))

    def shopping_cart(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Shopping Cart']")))

    def field_serch(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#search")))

    def phone(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".fa-phone")))
