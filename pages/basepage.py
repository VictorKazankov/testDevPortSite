from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def get_element_present(self, how, what):
        try:
            element = WebDriverWait(self.browser, timeout=4).until(EC.visibility_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return element
