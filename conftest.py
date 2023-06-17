import pytest
from selenium import webdriver
import os
import requests


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser")
    parser.addoption("--driver_storage", default=os.path.expanduser("~/dev/drivers"), help="Storage browser")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://141.105.64.208:8081", help="localhost")


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
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
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


@pytest.fixture(scope="session", autouse=True)
def api_token():
    s = requests.Session()
    username = "api_name"
    key = "RsotqZJtY25KpLzmb44vlOatBUSK5d5ZRU4XMq1yhiQvvC5Ghc58aQRO5EMcY3veoQL1UseVAmYU5277iUV37UrJv7b7xM2rsL21VZ1s81or5ujC5fV64YYnh4d3fjbKx1l8J1cKwsnAwdIslYmsnX6xxhnrPXDYConUE7DqX2sQsO66c4y4nvLdzD1UwUVnJeag3URx76FGlnBvWcsgDl6XIlDgUfBAol3uXY2H4e65VHY4YPl7AYcXwxrzKmTJ"
    t = s.post(
        "http://141.105.64.208:8081/index.php?route=api/login",
        data={"username": username, "key": key}).json()
    api_token = t['api_token']
    return api_token


@pytest.fixture(scope="session", autouse=True)
def config():
    return {"base_url": "http://141.105.64.208:8081/index.php?route="}
