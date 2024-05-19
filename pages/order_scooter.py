from locators.locators import ScooterLocatorsOrder as Locators
from data import ScooterLoginUp as Login
from selenium.webdriver.support.ui import WebDriverWait
import time
import allure



class ScooterOrder:


    def __init__(self, driver):
        self.driver = driver

    def open_cookies_popup(self):
        cookies_button = self.driver.find_element(*Locators.COOKIES_BUTTON)
        cookies_button.click()

    def click_order_button_up(self):
        order_button_up = self.driver.find_element(*Locators.ORDER_BUTTON_UP)
        order_button_up.click()

    def click_order_button_down(self):
        order_button_down = self.driver.find_element(*Locators.ORDER_BUTTON_DOWN)
        order_button_down.click()

    def send_keys_to_placeholder_name(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_NAME)
        placeholder_name.send_keys(*Login.LOGIN)

    def send_keys_to_placeholder_name_2(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_NAME)
        placeholder_name.send_keys(*Login.LOGIN_2)

    def send_keys_to_placeholder_surname(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_SURNEME)
        placeholder_name.send_keys(*Login.SURNAME)

    def send_keys_to_placeholder_surname_2(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_SURNEME)
        placeholder_name.send_keys(*Login.SURNAME_2)


    def send_keys_to_placeholder_adress(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_ADRESS)
        placeholder_name.send_keys(*Login.ADRESS)

    def send_keys_to_placeholder_adress_2(self):
        placeholder_name = self.driver.find_element(*Locators.PLACEHOLDER_ADRESS)
        placeholder_name.send_keys(*Login.ADRESS_2)

    def click_metro_field(self):
        metro_field = self.driver.find_element(*Locators.PLACEHOLDER_METRO)
        metro_field.click()

    def click_metro_choos_1(self):
        metro_choos_1 = self.driver.find_element(*Locators.METRO_3)
        metro_choos_1.click()

    def click_metro_choos_2(self):
        metro_choos_1 = self.driver.find_element(*Locators.METRO_4)
        metro_choos_1.click()

    def send_keys_to_placeholder_phone(self):
        placeholder_phone = self.driver.find_element(*Locators.PLACEHOLDER_PHONE)
        placeholder_phone.send_keys(*Login.PHONE)

    def send_keys_to_placeholder_phone_2(self):
        placeholder_phone = self.driver.find_element(*Locators.PLACEHOLDER_PHONE)
        placeholder_phone.send_keys(*Login.PHONE_2)



    def click_next_button(self):
        next_button = self.driver.find_element(*Locators.BUTTON_NEXT)
        next_button.click()

    def click_when_field(self):
        when_field = self.driver.find_element(*Locators.PLACEHOLDER_WHEN)
        when_field.click()

    def click_data_1_choos(self):
        data_1_choos = self.driver.find_element(*Locators.DATA)
        data_1_choos.click()

    def click_placeholder_data(self):
        placeholder_data = self.driver.find_element(*Locators.PLACEHOLDER_DATA)
        placeholder_data.click()

    def click_placeholder_order_time(self):
        laceholder_order_time = self.driver.find_element(*Locators.PLACEHOLDER_ORDER_TIME)
        laceholder_order_time.click()

    def click_yes_popup_button(self):
        yes_popup_button = self.driver.find_element(*Locators.BUTTON_YES_POP_UP)
        yes_popup_button.click()

    def wait(self):
        time.sleep(3)

    def order_placed(self):
        self.driver.find_element(*Locators.ORDER_PLACED)
        order_placed = self.driver.find_element(*Locators.ORDER_PLACED)
        return order_placed.text
