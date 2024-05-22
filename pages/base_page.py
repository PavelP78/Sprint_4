
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import ScooterLocatorsMainPage

class ScooterBasePage:

    def __init__(self, driver):
        self.driver = driver

    def cookies_popup(self):
        self.click_to_element(ScooterLocatorsMainPage.COOKIES_BUTTON)

    def click_order_button_up(self):
        self.click_to_element(ScooterLocatorsMainPage.ORDER_BUTTON_UP)

    def click_order_button_down(self):
        self.click_to_element(ScooterLocatorsMainPage.ORDER_BUTTON_DOWN)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        self.find_element(locator).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def set_text(self, locator, text):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)
    def tab_switch(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_url(self):
        return self.driver.current_url
