import pytest
from selenium import webdriver
import os


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser")
    parser.addoption("--driver_storage", default=os.path.expanduser("~/dev/drivers"), help="Storage browser")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://192.168.168.233:8081", help="localhost")


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver_storage = request.config.getoption("--driver_storage")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--url")

    _driver = None

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = headless
        _driver = webdriver.Chrome(executable_path=f"{driver_storage}/chromedriver", options=options)
    elif browser_name == "firefox" or browser_name == "ff":
        options = webdriver.FirefoxOptions()
        options.headless = headless
        _driver = webdriver.Firefox(executable_path=f"{driver_storage}/geckodriver", options=options)
    elif browser_name == "safari":
        _driver = webdriver.Safari()

    _driver.url = base_url
    _driver.maximize_window()
    yield _driver

    _driver.close()
