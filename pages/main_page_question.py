from locators.locators import ScooterLocatorsQuestion as Locators



class ScooterMainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_cookies_popup(self):
        cookies_button = self.driver.find_element(*Locators.COOKIES_BUTTON)
        cookies_button.click()

    def click_question_1_button(self):
        question_1_button = self.driver.find_element(*Locators.QUESTION_1_BUTTON)
        question_1_button.click()

    def get_answer_1(self):
        self.driver.find_element(*Locators.ANSWER_1)
        answer_1 = self.driver.find_element(*Locators.ANSWER_1)
        return answer_1.text


    def click_question_2_button(self):
        question_2_button = self.driver.find_element(*Locators.QUESTION_2_BUTTON)
        question_2_button.click()

    def get_answer_2(self):
        self.driver.find_element(*Locators.ANSWER_2)
        answer_2 = self.driver.find_element(*Locators.ANSWER_2)
        return answer_2.text

    def click_question_3_button(self):
        question_3_button = self.driver.find_element(*Locators.QUESTION_3_BUTTON)
        question_3_button.click()

    def get_answer_3(self):
        self.driver.find_element(*Locators.ANSWER_3)
        answer_3 = self.driver.find_element(*Locators.ANSWER_3)
        return answer_3.text

#4
    def click_question_4_button(self):
        question_4_button = self.driver.find_element(*Locators.QUESTION_4_BUTTON)
        question_4_button.click()

    def get_answer_4(self):
        self.driver.find_element(*Locators.ANSWER_4)
        answer_4 = self.driver.find_element(*Locators.ANSWER_4)
        return answer_4.text

#5
    def click_question_5_button(self):
        question_5_button = self.driver.find_element(*Locators.QUESTION_5_BUTTON)
        question_5_button.click()

    def get_answer_5(self):
        self.driver.find_element(*Locators.ANSWER_5)
        answer_5 = self.driver.find_element(*Locators.ANSWER_5)
        return answer_5.text

#6
    def click_question_6_button(self):
        question_6_button = self.driver.find_element(*Locators.QUESTION_6_BUTTON)
        question_6_button.click()

    def get_answer_6(self):
        self.driver.find_element(*Locators.ANSWER_6)
        answer_6 = self.driver.find_element(*Locators.ANSWER_6)
        return answer_6.text

#7
    def click_question_7_button(self):
        question_7_button = self.driver.find_element(*Locators.QUESTION_7_BUTTON)
        question_7_button.click()

    def get_answer_7(self):
        self.driver.find_element(*Locators.ANSWER_7)
        answer_7 = self.driver.find_element(*Locators.ANSWER_7)
        return answer_7.text

#8
    def click_question_8_button(self):
        question_8_button = self.driver.find_element(*Locators.QUESTION_8_BUTTON)
        question_8_button.click()

    def get_answer_8(self):
        self.driver.find_element(*Locators.ANSWER_8)
        answer_8 = self.driver.find_element(*Locators.ANSWER_8)
        return answer_8.text
