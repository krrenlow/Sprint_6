import allure
from Locators.main_page_locators import MainPageLocators
from page_object.check_base_page import BasePage


class CheckLogoScooter(BasePage):
    @allure.step("Нажать верхнюю кнопку Заказа")
    def click_order_button_top(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать логин Самокат")
    def click_scooter_logo(self):
        self.wait_for_element(MainPageLocators.LOGO_SCOOTER)
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Проверить, что открылась главная страница сайта ЯндексСамокат")
    def check_current_url_is_home_page(self, home_url):
        current_url = self.get_current_url()
        assert current_url == home_url

class CheckLogoYandex(BasePage):
    @allure.step("Нажать логин Яндекс")
    def click_yandex_logo(self):
        self.wait_for_element(MainPageLocators.LOGO_YANDEX)
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Проверить, что открылась главная страница Дзен")
    def check_current_url_is_home_page(self, home_url):
        current_url = self.get_current_url()
        assert current_url == home_url