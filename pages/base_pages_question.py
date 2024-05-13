from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageQuestion:

    question_1 = [By.ID, '//div[@class="accordion__button"]']
    ANSWER_1 = (By.ID, '//p[contains(text(), "400 рублей")]')


    def clik_question_1_button(self):
        driver.find_element(*question_1).clik()


    def check_answer_question_1(self, question_1):
        actually_answer = self.driver.find_element(*question_1).clik()
        active_text = driver.find_element(*ANSWER_1).text
        assert active_text == '400 рублей'
