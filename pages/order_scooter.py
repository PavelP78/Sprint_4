import allure

from locators.locators import ScooterLocatorsOrder as Locators
from pages.base_page import ScooterBasePage
from data import ScooterLoginUp as Login

class ScooterOrderPage(ScooterBasePage):

    @allure.step(f"Заполнение формы имя: {Login.LOGIN}")
    def send_keys_to_placeholder_name(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_NAME)
        placeholder_name.send_keys(*Login.LOGIN)


    @allure.step(f"Заполнение формы имя: {Login.SURNAME_2}")
    def send_keys_to_placeholder_name_2(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_NAME)
        placeholder_name.send_keys(*Login.LOGIN_2)


    @allure.step(f"Заполнение формы фамилия: {Login.SURNAME}")
    def send_keys_to_placeholder_surname(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_SURNEME)
        placeholder_name.send_keys(*Login.SURNAME)

    @allure.step(f"Заполнение формы фамилия: {Login.SURNAME_2}")
    def send_keys_to_placeholder_surname_2(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_SURNEME)
        placeholder_name.send_keys(*Login.SURNAME_2)

    @allure.step(f"Заполнение формы адрес: {Login.ADRESS}")
    def send_keys_to_placeholder_adress(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_ADRESS)
        placeholder_name.send_keys(*Login.ADRESS)

    @allure.step(f"Заполнение формы адрес: {Login.ADRESS_2}")
    def send_keys_to_placeholder_adress_2(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_ADRESS)
        placeholder_name.send_keys(*Login.ADRESS_2)

    @allure.step("Заполнение формы метро")
    def click_metro_field(self):
        metro_field = self.driver.find_element(*Locators.PLACEHOLDER_METRO)
        metro_field.click()

    @allure.step("Выбор станции метро: Преображенская площадь")
    def click_metro_choos_1(self):
        metro_choos_1 = self.driver.find_element(*Locators.METRO_3)
        metro_choos_1.click()

    @allure.step("Выбор станции метро: Сокольники")
    def click_metro_choos_2(self):
        metro_choos_1 = self.driver.find_element(*Locators.METRO_4)
        metro_choos_1.click()

    @allure.step(f"Заполнение формы телефон: {Login.PHONE}")
    def send_keys_to_placeholder_phone(self):
        placeholder_phone = self.driver.find_element(*Locators.PLACEHOLDER_PHONE)
        placeholder_phone.send_keys(*Login.PHONE)

    @allure.step(f"Заполнение формы телефон: {Login.PHONE_2}")
    def send_keys_to_placeholder_phone_2(self):
        placeholder_phone = self.driver.find_element(*Locators.PLACEHOLDER_PHONE)
        placeholder_phone.send_keys(*Login.PHONE_2)

    @allure.step("Нажатие кнопки Далее")
    def click_next_button(self):
        next_button = self.driver.find_element(*Locators.BUTTON_NEXT)
        next_button.click()

    @allure.step("Нажатие на поле Когда привезти самокат")
    def click_when_field(self):
        when_field = self.driver.find_element(*Locators.PLACEHOLDER_WHEN)
        when_field.click()

    @allure.step("Выбор даты доставки")
    def click_data_1_choos(self):
        data_1_choos = self.driver.find_element(*Locators.DATA)
        data_1_choos.click()

    @allure.step("Нажатие на поле Срок аренды")
    def click_placeholder_data(self):
        placeholder_data = self.driver.find_element(*Locators.PLACEHOLDER_DATA)
        placeholder_data.click()

    @allure.step("Выбор срока аренды")
    def click_placeholder_order_time(self):
        placeholder_order_time = self.driver.find_element(*Locators.PLACEHOLDER_ORDER_TIME)
        placeholder_order_time.click()

    @allure.step("Нажатие кнопки Да")
    def click_yes_popup_button(self):
        yes_popup_button = self.driver.find_element(*Locators.BUTTON_YES_POP_UP)
        yes_popup_button.click()

    @allure.step("Получение подтверждения заказа")
    def order_placed(self):
        self.driver.find_element(*Locators.ORDER_PLACED)
        order_placed = self.driver.find_element(*Locators.ORDER_PLACED)
        return order_placed.text