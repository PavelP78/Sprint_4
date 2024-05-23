from locators.locators import ScooterLocatorsMainPage
from pages.base_page import ScooterBasePage
import allure

class MainPageScooter(ScooterBasePage):

    @allure.step('Нажатие лого Яндекса')
    def click_logo_yandex(self):
        self.click_to_element(ScooterLocatorsMainPage.LOGO_YANDEX)

    @allure.step('Проверка страницы Яндекс Дзен')
    def get_dzen_news(self):
        return self.find_element(ScooterLocatorsMainPage.DZEN_NEWS)

    @allure.step('Нажатие лого Самокат')
    def click_logo_scooter(self):
        self.click_to_element(ScooterLocatorsMainPage.LOGO_SCOOTER)

