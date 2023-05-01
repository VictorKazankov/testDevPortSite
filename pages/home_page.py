import time

from pages.basepage import BasePage
from pages.locators import Locators


class HomePage(BasePage):
    def open(self):
        self.browser.get(self.url)
        assert "DevPort" in self.browser.title

    def get_about_us_title(self):
        return self.get_element_present(*Locators.ABOUT_TITLE)

    def is_displayed_astroman_image(self):
        self.get_element_present(*Locators.ASTROMAN_IMAGE_1920)

    def get_vacancies_title(self):
        return self.get_element_present(*Locators.VACANCIES_TITLE)

    def is_displayed_vacancies_site(self):
        # get current window handle
        current_site = self.browser.current_window_handle
        # get all handles
        handles = self.browser.window_handles
        for tap in handles:
            # switch focus to child window
            if tap != current_site:
                self.browser.switch_to.window(tap)
                break

        time.sleep(1)
        assert self.browser.title == "DevPort Careers"
