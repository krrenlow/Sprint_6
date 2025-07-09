from selenium.webdriver.common.by import By

class OrderStatusPageLocators:
    # Поле "Статус заказа"
    ORDER_STATUS = (By.XPATH, "//input[@value='{order_number}']")