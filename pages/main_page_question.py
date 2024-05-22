from locators.locators import ScooterLocatorsMainPage
from pages.base_page import ScooterBasePage
import allure

class MainPageScooterQuestion(ScooterBasePage):

    @allure.step('Просмотр вопросов')
    def clik_quession(self, number):
        method, locator = ScooterLocatorsMainPage.QUESTION
        locator = locator.format(number)
        self.find_element((method, locator))
        return self.click_to_element((method, locator))

    @allure.step('Просмотр ответов')
    def get_answer(self, number):
        method, locator = ScooterLocatorsMainPage.ANSWER
        locator = locator.format(number)
        self.find_element((method, locator))
        return self.get_text((method, locator))

