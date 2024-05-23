from pages.main_page_logo import MainPageScooter
from data import ScooterUrl as Url
from conftest import driver
import allure

class TestScooterLogo:

    @allure.title('Проверка логотипа Самоката')
    def test_scooter_logo_scooter(self, driver):
        main_page_scooter = MainPageScooter(driver)
        main_page_scooter.cookies_popup()
        main_page_scooter.click_logo_scooter()
        assert Url.URL_MAIN == main_page_scooter.get_url()
    @allure.title('Проверка логотипа Яндекс')
    def test_scooter_logo_yandex(self, driver):
        main_page_scooter = MainPageScooter(driver)
        main_page_scooter.cookies_popup()
        main_page_scooter.click_logo_yandex()
        main_page_scooter.tab_switch()
        main_page_scooter.get_dzen_news()
        assert Url.URL_DZEN in main_page_scooter.get_url()
