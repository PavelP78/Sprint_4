from locators.locators import ScooterLogo as Locators
import time
import allure



class ScooterLogo:


    def __init__(self, driver):
        self.driver = driver


    def open_cookies_popup(self):
            cookies_button = self.driver.find_element(*Locators.COOKIES_BUTTON)
            cookies_button.click()

    def wait(self):
        time.sleep(5)


    def click_logo_yandex(self):
        logo_yandex = self.driver.find_element(*Locators.LOGO_YANDEX)
        logo_yandex.click()

    def dzen_window(self):
        self.driver.find_element(*Locators.BUTTON_FIND)
        dzen_window = self.driver.find_element(*Locators.BUTTON_FIND)
        return dzen_window.text

    def click_order_button_up(self):
        order_button_up = self.driver.find_element(*Locators.ORDER_BUTTON_UP)
        order_button_up.click()

    def click_logo_scooter(self):
        logo_scooter = self.driver.find_element(*Locators.LOGO_SCOOTER)
        logo_scooter.click()

    def click_question_1_button(self):
        question_1_button = self.driver.find_element(*Locators.QUESTION_1_BUTTON)
        question_1_button.click()

    def get_answer_1(self):
        self.driver.find_element(*Locators.ANSWER_1)
        answer_1 = self.driver.find_element(*Locators.ANSWER_1)
        return answer_1.text
