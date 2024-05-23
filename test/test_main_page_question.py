from pages.main_page_question import MainPageScooterQuestion
from conftest import driver
import allure
from data import QuestionAnswer
import pytest

class TestScooterQuestion:
    @allure.title('Проверка соответствия вопросов и ответов')
    @pytest.mark.parametrize('number, expected_answer', QuestionAnswer.answers)
    def test_main_page_question(self, driver, number, expected_answer):
        main_page_question = MainPageScooterQuestion(driver)
        main_page_question.cookies_popup()
        main_page_question.clik_quession(number)
        answer = main_page_question.get_answer(number)
        assert answer == expected_answer
