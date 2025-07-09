import allure

from page_object.check_logo import CheckLogoScooter, CheckLogoYandex
from urls import *

class TestCheckLogoScooter:
    @allure.step("Тест на проверку логотипа Самокат")
    def test_check_logo_scooter(self, driver):
        check_logo = CheckLogoScooter(driver)
        check_logo.click_order_button_top()
        check_logo.click_scooter_logo()
        check_logo.check_current_url_is_home_page(home_page)

    @allure.step("Тест на проверку логотипа Яндекс")
    def test_check_logo_yandex(self, driver):
        check_logo = CheckLogoYandex(driver)
        check_logo.click_yandex_logo()
        check_logo.check_current_url_is_home_page(page_dzen)

