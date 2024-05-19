from pages.logo import ScooterLogo
import allure

class TestScooterOrder:


    # @allure.title("logo_yandex")
    # def test_scooter_logo_yandex(self, driver):
    #     page = ScooterLogo(driver)
    #     page.open_cookies_popup()
    #     page.click_logo_yandex()
    #     driver.switch_to.window(driver.window_handles[1])
    #     page.dzen_window()
    #     find_button = page.dzen_window()
    #     assert  "Найти" in find_button


    def test_scooter_logo_scooter(self, driver):
        page = ScooterLogo(driver)
        page.open_cookies_popup()
        page.click_order_button_up()
        page.click_logo_scooter()
        page.click_question_1_button()
        question_1 = page.get_answer_1()
        assert 'Сутки — 400 рублей.' in question_1
