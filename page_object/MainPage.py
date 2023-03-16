from config import time_sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage():
    def __init__(self,driver):
        self.driver = driver

    def open_page(self):
        PAGE_NAME = "/index.php"
        self.driver.get(self.driver.url + PAGE_NAME)

    def form_contact_us(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content")))