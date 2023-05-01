from selenium.webdriver.common.by import By


class Locators:
    ABOUT_TITLE = (By.XPATH, "//div[@class='nav desktop']/a")
    ASTROMAN_IMAGE_1920 = (By.XPATH, "//img[@src='/build/img/astromanWeAre.svg']") # for resolution 1920
    VACANCIES_TITLE = (By.XPATH, "//div[@class='nav desktop']/a[@target='_blank']")