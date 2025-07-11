import allure

from page_object.check_logo import CheckLogoScooter, CheckLogoYandex
from urls import *

class TestCheckLogoScooter:
    @allure.title("Проверка перехода на главную страницу через логотип Самоката")
    @allure.description("""
     Тест проверяет, что при нажатии на логотип Самоката 
     происходит переход на главную страницу сервиса.
     Шаги:
     1. Нажать на кнопку заказа вверху страницы
     2. Нажать на логотип Самоката
     3. Проверить, что текущий URL соответствует главной странице
     """)
    def test_check_logo_scooter(self, driver):
        check_logo = CheckLogoScooter(driver)
        check_logo.click_order_button_top()
        check_logo.click_scooter_logo()
        check_logo.check_current_url_is_home_page(home_page)

    @allure.title("Проверка перехода на Дзен через логотип Яндекс")
    @allure.description("""
      Тест проверяет, что при нажатии на логотип Яндекс
      происходит переход на страницу Дзен.
      Шаги:
      1. Нажать на логотип Яндекс
      2. Проверить, что текущий URL соответствует странице Дзен
      """)
    def test_check_logo_yandex(self, driver):
        check_logo = CheckLogoYandex(driver)
        check_logo.click_yandex_logo()
        check_logo.check_current_url_is_home_page(page_dzen)

