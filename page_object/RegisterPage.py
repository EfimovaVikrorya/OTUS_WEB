from config import time_sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage():
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        PAGE_NAME = "/index.php?route=account/register"
        self.driver.get(self.driver.url + PAGE_NAME)

    def house(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))

    def set_firstname(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))

    def set_lastname(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))

    def set_email(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")))

    def set_telephone(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-telephone")))

    def set_password(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))

    def set_confirm_password(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-confirm")))

    def click_btn_continue(self):
        el_btn_cont = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
        el_btn_cont.click()
