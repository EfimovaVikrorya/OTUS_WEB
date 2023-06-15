from config import time_sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HederElement:
    def __init__(self, driver):
        self.driver = driver

    def logo(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".img-responsive")))

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

    def dropdown_currency(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#form-currency .dropdown-toggle")))

    def GBP_currency(self):
        dr_cur = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#form-currency .dropdown-toggle")))
        dr_cur.click()
        btn_GBP = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".currency-select[name = 'GBP']")))
        btn_GBP.click()
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#form-currency .dropdown-toggle strong")))

    def Euro_currency(self):
        dr_cur = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#form-currency .dropdown-toggle")))
        dr_cur.click()
        btn_EUR = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".currency-select[name = 'EUR']")))
        btn_EUR.click()
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#form-currency .dropdown-toggle strong")))

    def USD_currency(self):
        dr_cur = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#form-currency .dropdown-toggle")))
        dr_cur.click()
        btn_USD = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".currency-select[name = 'USD']")))
        btn_USD.click()
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#form-currency .dropdown-toggle strong")))
