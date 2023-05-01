class TestHeaderElements:
    def test_about_us_elements_text(self, home_page):
        about_us_element = home_page.get_about_us_title()
        assert about_us_element.text == "Про нас"

    def test_is_displayed_about_us_section(self, home_page):
        about_us_element = home_page.get_about_us_title()
        about_us_element.click()
        home_page.is_displayed_astroman_image()

    def test_is_displayed_vacancies_site(self, home_page):
        vacancies_element = home_page.get_vacancies_title()
        vacancies_element.click()
        home_page.is_displayed_vacancies_site()

