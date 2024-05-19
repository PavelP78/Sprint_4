# from pages.main_page_question import ScooterMainPage
#
#
# class TestScooterQuestion:
#
#     def test_main_page_qestion_1(self, driver):
#         page = ScooterMainPage(driver)
#         page.open_cookies_popup()
#         page.click_question_1_button()
#         question_1 = page.get_answer_1()
#         assert 'Сутки — 400 рублей.' in question_1
#
#     def test_main_page_qestion_2(self, driver):
#         page = ScooterMainPage(driver)
#         page.open_cookies_popup()
#         page.click_question_2_button()
#         question_2 = page.get_answer_2()
#         assert 'один самокат' in question_2
#
#     def test_main_page_qestion_3(self, driver):
#         page = ScooterMainPage(driver)
#         page.open_cookies_popup()
#         page.click_question_3_button()
#         question_3 = page.get_answer_3()ё
#         assert '8 мая в 20:30' in question_3
#
#     def test_main_page_qestion_4(self, driver):
#         page = ScooterMainPage(driver)
#         page.open_cookies_popup()
#         page.click_question_4_button()
#         question_4 = page.get_answer_4()
#         assert 'с завтрашнего дня' in question_4
#
#     def test_main_page_qestion_5(self, driver):
#         page = ScooterMainPage(driver)
#         page.open_cookies_popup()
#         page.click_question_5_button()
#         question_5 = page.get_answer_5()
#         assert 'что-то срочное' in question_5
#
#     def test_main_page_qestion_6(self, driver):
#         page = ScooterMainPage(driver)
#         page.open_cookies_popup()
#         page.click_question_6_button()
#         question_6 = page.get_answer_6()
#         assert 'на восемь суток' in question_6
#
#     def test_main_page_qestion_7(self, driver):
#         page = ScooterMainPage(driver)
#         page.open_cookies_popup()
#         page.click_question_7_button()
#         question_7 = page.get_answer_7()
#         assert 'Все же свои.' in question_7
#
#     def test_main_page_qestion_8(self, driver):
#         page = ScooterMainPage(driver)
#         page.open_cookies_popup()
#         page.click_question_8_button()
#         question_8 = page.get_answer_8()
#         assert 'И Москве' in question_8
