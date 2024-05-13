from selenium.webdriver.common.by import By

class ScooterLocators:

    LOGO = (By.XPATH, '//div[contains(@class,"Header_Logo")]')  # Лого яндекс на главной странице сайта скутер

    DZEN_MAIN_BUTTON = (By.XPATH, '//button[@class="arrow__button"]')  # Кнопка "НАЙТИ" на главной странице яндекс-дзен

    QUESTION_1_BUTTON = (By.XPATH, '//div[@class="accordion__button"]')  # Кнопка первого вопроса главная страница
    ANSWER_1 = (By.XPATH, '//p[contains(text(), "400 рублей")]')  # Ответ на первый вопрос

