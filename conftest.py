import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.home_page import HomePage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


def change_browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # resolved warning of certificate
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unrecognized browser {browser_name}")
    return driver


@pytest.fixture(scope="session")
def browser(request):
    browser = change_browser(request)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def home_page(browser):
    home_page = HomePage(browser, "https://devport.io/")
    home_page.open()
    return home_page
