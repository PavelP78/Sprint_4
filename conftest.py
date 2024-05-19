import pytest
from selenium import webdriver
from data import ScooterUrl as Url



@pytest.fixture
def driver():
     driver = webdriver.Firefox()
     driver.maximize_window()
     driver.get(Url.URL_MAIN)


     driver.delete_all_cookies()

     yield driver

     driver.quit()

