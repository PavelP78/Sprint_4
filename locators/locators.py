from selenium.webdriver.common.by import By

class ScooterLocatorsMainPage:

    COOKIES_BUTTON = (By.XPATH, '//button[@class="App_CookieButton__3cvqF"]')  # Кнопка куки на гл странице
    ORDER_BUTTON_UP = (By.XPATH, '//button[@class="Button_Button__ra12g"]')  # кнопка ЗАКАЗАТЬ на главной странице наверху
    ORDER_BUTTON_DOWN = (By.XPATH,'//button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]')  # кнопка ЗАКАЗАТЬ на главной странице внизу
    LOGO_SCOOTER = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')  # logo скутер главной странице
    LOGO_YANDEX = [By.XPATH, "//a[contains(@class,'Header_LogoYandex')]/img"] # logo yandex  главной странице
    DZEN_NEWS = (By.XPATH, '//div[contains(text(),"Новости")]') #  главной страница дзена - новости
    QUESTION = By.XPATH, "//div[@id = 'accordion__heading-{}']" # вопросы на главной странице
    ANSWER = By.XPATH, '//div[@id="accordion__panel-{}"]/p' # ответы на главной странице

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
