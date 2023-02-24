from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGE_NAME = "/admin"


class Config:
    FAST = 1
    NORM = 2
    SLOW = 3
    VERY_SLOW = 4


def test_admin_empty_credits(driver):
    driver.get(driver.url + PAGE_NAME)
    el_user = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-username")))
    el_pwd = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-password")))
    assert el_user.text == ''
    assert el_pwd.text == ''


def test_admin_alias_invalid_password(driver):
    driver.get(driver.url + PAGE_NAME)
    el_user = WebDriverWait(driver, Config.FAST, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-username")))
    el_user.send_keys('fghhgg')
    el_pwd = WebDriverWait(driver, Config.FAST, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-password")))
    el_pwd.send_keys('5678777')
    for i in range(10):
        batton = WebDriverWait(driver, Config.VERY_SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".fa-key")))
        batton.click()
    el_alert = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    assert el_alert.text == 'Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour or reset password.\n×'


def test_admin_logo(driver):
    driver.get(driver.url + PAGE_NAME)
    WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-brand")))


def test_admin_text_forgotten_password(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".help-block")))
    assert el.text == "Forgotten Password"


def test_click_btn_login_when_enpty_credits(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-key")))
    el.click()
    el_alert = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    assert el_alert.text == 'No match for Username and/or Password.\n×'
