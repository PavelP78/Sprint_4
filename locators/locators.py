from selenium.webdriver.common.by import By

class ScooterLocatorsQuestion:


    COOKIES_BUTTON = (By.XPATH, '//button[@class="App_CookieButton__3cvqF"]')  # Кнопка куки на гл странице


    QUESTION_1_BUTTON = (By.XPATH, '//div[@class="accordion__button" and text()= "Сколько это стоит? И как оплатить?"]')  # Кнопка 1 вопроса главная страница
    ANSWER_1 = (By.XPATH, '//p[contains(text(), "Сутки — 400 рублей")]')  # Ответ на 1 вопрос

    QUESTION_2_BUTTON = (By.XPATH, '//div[@class="accordion__button" and text()= "Хочу сразу несколько самокатов! Так можно?"]')  # Кнопка 2 вопроса главная страница
    ANSWER_2 = (By.XPATH, '//p[contains(text(), "Пока что у нас так:")]')  # Ответ на 2 вопрос

    QUESTION_3_BUTTON = (By.XPATH, '//div[@class="accordion__button" and text()= "Как рассчитывается время аренды?"]')  # Кнопка 3 вопроса главная страница
    ANSWER_3 = (By.XPATH, '//p[contains(text(), "Допустим, вы оформляете заказ на 8 мая")]')  # Ответ на 3 вопрос

    QUESTION_4_BUTTON = (By.XPATH, '//div[@class="accordion__button" and text()= "Можно ли заказать самокат прямо на сегодня?"]')  # Кнопка 4 вопроса главная страница
    ANSWER_4 = (By.XPATH, '//p[contains(text(), "скоро станем расторопнее")]')  # Ответ на 4 вопрос

    QUESTION_5_BUTTON = (By.XPATH, '//div[@class="accordion__button" and text()= "Можно ли продлить заказ или вернуть самокат раньше?"]')  # Кнопка 5 вопроса главная страница
    ANSWER_5 = (By.XPATH, '//p[contains(text(), "Пока что нет!")]')  # Ответ на 5 вопрос

    QUESTION_6_BUTTON = (By.XPATH, '//div[@class="accordion__button" and text()= "Вы привозите зарядку вместе с самокатом?"]')  # Кнопка 6 вопроса главная страница
    ANSWER_6 = (By.XPATH, '//p[contains(text(), "Зарядка не понадобится.")]')  # Ответ на 6 вопрос

    QUESTION_7_BUTTON = (By.XPATH, '//div[@class="accordion__button" and text()= "Можно ли отменить заказ?"]')  # Кнопка 7 вопроса главная страница
    ANSWER_7 = (By.XPATH, '//p[contains(text(), "Штрафа не будет")]')  # Ответ на 7 вопрос

    QUESTION_8_BUTTON = (By.XPATH, '//div[@class="accordion__button" and text()= "Я жизу за МКАДом, привезёте?"]')  # Кнопка 8 вопроса главная страница
    ANSWER_8= (By.XPATH, '//p[contains(text(), "Всем самокатов!")]')  # Ответ на 8 вопрос

class ScooterLocatorsOrder:

    COOKIES_BUTTON = (By.XPATH, '//button[@class="App_CookieButton__3cvqF"]')  # Кнопка куки на гл странице

    ORDER_BUTTON_UP = (By.XPATH, '//button[@class="Button_Button__ra12g"]')  # кнопка ЗАКАЗАТЬ на главной странице наверху
    ORDER_BUTTON_DOWN = (By.XPATH,'//button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]')  # кнопка ЗАКАЗАТЬ на главной странице внизу

    PLACEHOLDER_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')  # плейсхолдер Имя
    PLACEHOLDER_SURNEME = (By.XPATH, '//input[@placeholder="* Фамилия"]')  # плейсхолдер Фамилия
    PLACEHOLDER_ADRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')  # плейсхолдер адреса
    PLACEHOLDER_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')  # плейсхолдер метро
    PLACEHOLDER_PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')  # плейсхолдер номер телефона

    BUTTON_NEXT = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')  # кнопка Далее
    PLACEHOLDER_WHEN = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')  # плейсхолдер когда привезти
    PLACEHOLDER_TIME = (By.XPATH, '//div[@class="Dropdown-placeholder"]')  # плейсхолдер срок аренды
    PLACEHOLDER_BLACK = (By.XPATH, '//input[@id="black"]')  # плейсхолдер черный жемчуг
    PLACEHOLDER_GREY = (By.XPATH, '//input[@id="grey"]')  # плейсхолдер серая бызысходность
    PLACEHOLDER_COMMENT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')  # плейсхолдер комментарий для курьера
    BUTTON_FINAL_ORDER = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')  # пкнопка ЗАКАЗАТЬ на странице заказа
    BUTTON_BACK = (By.XPATH,'//button[@class="Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i" and text()="Назад"]')  # кнопка назад а странице заказа

    PLACEHOLDER_DATA = (By.XPATH,'//div[@class="Dropdown-placeholder" and text()="* Срок аренды"]')  # плейсхолдер срок аренды
    PLACEHOLDER_ORDER_TIME = (By.XPATH, '//div[@class="Dropdown-option" and text()="четверо суток"]')  # плейсхолдер срок 4 суток
    BUTTON_YES_POP_UP = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]')  # кнопка ДА

    METRO_3 = (By.XPATH, '//div[@class="Order_Text__2broi" and text()="Преображенская площадь"]')  # Преображенская площадь
    METRO_4 = (By.XPATH, '//div[@class="Order_Text__2broi" and text()="Сокольники"]')  # Преображенская площадь

    DATA = (By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--031"]')  #

    ORDER_PLACED = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ" and text()="Заказ оформлен"]')  # Преображенская площадь

class ScooterLogo:

    COOKIES_BUTTON = (By.XPATH, '//button[@class="App_CookieButton__3cvqF"]')  # Кнопка куки на гл странице
    LOGO_YANDEX = (By.XPATH, '//a[@href="//yandex.ru"]')  # Кнопка куки на гл странице

    BUTTON_FIND = (By.XPATH, '//button[@class="arrow__button" and text()="Найти"]')  # кнопка найти на главной странице дзена
    ORDER_BUTTON_UP = (By.XPATH, '//button[@class="Button_Button__ra12g"]')  # кнопка ЗАКАЗАТЬ на главной странице наверху


    LOGO_SCOOTER = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')  # кнопка ЗАКАЗАТЬ на главной странице наверху

    QUESTION_1_BUTTON = (By.XPATH, '//div[@class="accordion__button" and text()= "Сколько это стоит? И как оплатить?"]')  # Кнопка 1 вопроса главная страница
    ANSWER_1 = (By.XPATH, '//p[contains(text(), "Сутки — 400 рублей")]')  # Ответ на 1 вопрос
