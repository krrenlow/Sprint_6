from selenium.webdriver.common.by import By

class MainPageLocators:

    # Логотип "Яндекс"
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    # Логотип "Самокат"
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    # Верхняя кнопка "Заказа"
    ORDER_BUTTON_TOP = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    # Нижняя кнопка "Заказа"
    ORDER_BUTTON_LOWER = (By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")
    # Cookie
    COOKIE = [By.XPATH, "//button[text()='да все привыкли']"]


    # Список вопросов
    fag_questions_items = {
        0: (By.ID, "accordion__heading-0"),
        1: (By.ID, "accordion__heading-1"),
        2: (By.ID, "accordion__heading-2"),
        3: (By.ID, "accordion__heading-3"),
        4: (By.ID, "accordion__heading-4"),
        5: (By.ID, "accordion__heading-5"),
        6: (By.ID, "accordion__heading-6"),
        7: (By.ID, "accordion__heading-7")
    }
    # Список ответов
    faq_answers_items = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7")
    }

