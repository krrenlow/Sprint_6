from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Поле ввода "Имя"
    NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    # Поле ввода "Фамилии"
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Поле ввода "адреса"
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Поле ввода станции "метро"
    BUTTON_METRO = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]
    # Список станций "метро"
    BUTTON_METRO_ENTER =  (By.XPATH, ".//li[@class='select-search__row']")
    # Поле ввода "телефона"
    TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка "Далее"
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    # Поле ввода "Когда привезти самокат"
    WHEN_TO_BRING = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Поле ввода "Срок аренды"
    RENTAL_PERIOD = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    # Выпадающий список на форме
    NUMBER_OF_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    # Поле ввода "Цвет самоката"
    SCOOTER_COLOR = (By.ID, 'black')
    # Поле ввода "Комментарий"
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка "Заказать"
    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    # Кнопка "Да"в модальном окне "Хотите оформить заказ"
    PLACE_AN_ORDER = (By.XPATH, "//button[text()='Да']")
    # Кнопка в окне "Заказ оформлен", "Посмотреть статус"
    VIEW_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")
    # Проверить,что заказ создан
    ORDER_CHECK = (By.XPATH, "//div[@class='Input_InputContainer__3NykH']")


