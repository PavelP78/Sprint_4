import pytest
from selenium import webdriver
from config import ScooterResolution as Resolution
from data import ScooterUrl as Url

def browser_setting():
     firefox_option = webdriver.FirefoxOptions()
     firefox_option.add_argument(f'--window-size = {Resolution.RESOLUTION[0]}, {Resolution.RESOLUTION[1]}')
     return firefox_option

@pytest.fixture
def driver():
     firefox = webdriver.Firefox(options=browser_setting())
     firefox.get(Url.URL_MAIN)

     yield firefox

     firefox.quit()


# ======
# import pytest
# from selenium import webdriver
# from config import ScooterResolution as Resolution
# from data import ScooterUrl as Url

# def browser_setting():
#      chrome_option = webdriver.ChromeOptions()
#      chrome_option.add_argument(f'--window-size = {Resolution.RESOLUTION[0]}, {Resolution.RESOLUTION[1]}')
#      return chrome_option
#
# @pytest.fixture
# def driver():
#      chrome = webdriver.Chrome(options=browser_setting())
#      chrome.get(Url.URL_MAIN)
#
#      yield chrome
#
#      chrome.quit()

