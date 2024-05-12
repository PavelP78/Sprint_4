from locators.locators import ScooterLocators
from data import ScooterUrl as Url


class TestScooterYandexLogo:


    def test_main_page_logo(self, driver):
        assert driver.current_url == f'{Url.URL_MAIN}', "Url is wrong"