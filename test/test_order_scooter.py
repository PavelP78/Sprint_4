from pages.base_page import ScooterBasePage
from pages.order_scooter import ScooterOrderPage
import allure
class TestScooterOrder:

    @allure.title('Проверка заказа самоката через веркнюю кнопку "Заказать"')
    def test_scooter_order_use_up_button(self, driver):

        main_page_scooter = ScooterBasePage(driver)
        main_page_scooter.cookies_popup()
        main_page_scooter.click_order_button_up()

        order_scooter_page = ScooterOrderPage(driver)
        order_scooter_page.send_keys_to_placeholder_name()
        order_scooter_page.send_keys_to_placeholder_surname()
        order_scooter_page.send_keys_to_placeholder_adress()
        order_scooter_page.click_metro_field()
        order_scooter_page.click_metro_choos_1()
        order_scooter_page.send_keys_to_placeholder_phone()
        order_scooter_page.click_next_button()
        order_scooter_page.click_when_field()
        order_scooter_page.click_data_1_choos()
        order_scooter_page.click_placeholder_data()
        order_scooter_page.click_placeholder_order_time()
        order_scooter_page.click_next_button()
        order_scooter_page.click_yes_popup_button()
        placed_1 = order_scooter_page.order_placed()
        assert "Номер заказа:" in placed_1

    @allure.title('Проверка заказа самоката через нижнюю кнопку "Заказать"')
    def test_scooter_order_use_down_button(self, driver):

        main_page_scooter = ScooterBasePage(driver)
        main_page_scooter.cookies_popup()
        main_page_scooter.click_order_button_up()

        order_scooter_page = ScooterOrderPage(driver)
        order_scooter_page.send_keys_to_placeholder_name_2()
        order_scooter_page.send_keys_to_placeholder_surname_2()
        order_scooter_page.send_keys_to_placeholder_adress_2()
        order_scooter_page.click_metro_field()
        order_scooter_page.click_metro_choos_2()
        order_scooter_page.send_keys_to_placeholder_phone_2()
        order_scooter_page.click_next_button()
        order_scooter_page.click_when_field()
        order_scooter_page.click_data_1_choos()
        order_scooter_page.click_placeholder_data()
        order_scooter_page.click_placeholder_order_time()
        order_scooter_page.click_next_button()
        order_scooter_page.click_yes_popup_button()
        placed_1 = order_scooter_page.order_placed()
        assert "Номер заказа:" in placed_1
