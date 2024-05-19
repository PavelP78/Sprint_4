# from pages.order_scooter import ScooterOrder
#
# class TestScooterOrder:
#
#     def test_scooter_order_use_up_button(self, driver):
#         page = ScooterOrder(driver)
#         page.open_cookies_popup()
#         page.click_order_button_up()
#         page.send_keys_to_placeholder_name()
#         page.send_keys_to_placeholder_surname()
#         page.send_keys_to_placeholder_adress()
#         page.click_metro_field()
#         page.click_metro_choos_1()
#         page.send_keys_to_placeholder_phone()
#         page.click_next_button()
#         page.click_when_field()
#         page.click_data_1_choos()
#         page.click_placeholder_data()
#         page.click_placeholder_order_time()
#         page.click_next_button()
#         page.click_yes_popup_button()
#         placed_1 = page.order_placed()
#         assert "Номер заказа:" in placed_1
#
#
#     def test_scooter_order_use_down_button(self, driver):
#         page = ScooterOrder(driver)
#         page.open_cookies_popup()
#         page.click_order_button_up()
#         page.send_keys_to_placeholder_name_2()
#         page.send_keys_to_placeholder_surname_2()
#         page.send_keys_to_placeholder_adress_2()
#         page.click_metro_field()
#         page.click_metro_choos_2()
#         page.send_keys_to_placeholder_phone_2()
#         page.click_next_button()
#         page.click_when_field()
#         page.click_data_1_choos()
#         page.click_placeholder_data()
#         page.click_placeholder_order_time()
#         page.click_next_button()
#         page.click_yes_popup_button()
#         placed_1 = page.order_placed()
#         assert "Номер заказа:" in placed_1
#
#
