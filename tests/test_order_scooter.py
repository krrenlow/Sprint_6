import allure
from page_object.check_order import OrderScooter
import data



class TestOrderScooter:
    @allure.title("Проверка успешного заказа самоката через верхнюю кнопку 'Заказать'")
    @allure.description("""
    Тест проверяет полный процесс заказа самоката:
    1. Нажатие на верхнюю кнопку 'Заказать'
    2. Заполнение первой формы заказа (личные данные)
    3. Выбор станции метро
    4. Переход ко второй форме заказа
    5. Заполнение деталей аренды (дата, срок, цвет самоката, комментарий)
    6. Подтверждение заказа
    7. Проверка номера заказа
    """)
    def test_success_ful_order_first(self, driver):
        order_scooter = OrderScooter(driver)
        order_scooter.click_order_button_top()
        order_scooter.fill_first_order_form(data.OrderScooterFirst.name, data.OrderScooterFirst.surname, data.OrderScooterFirst.address, data.OrderScooterFirst.telephone)
        order_scooter.choose_metro(data.OrderScooterFirst.station_name)
        order_scooter.click_button_further()
        order_scooter.fill_second_order_form(data.OrderScooterFirst.date, data.OrderScooterFirst.comment)
        order_scooter.choose_rental_period()
        order_scooter.choose_scooter_color()
        order_scooter.click_button_order()
        order_scooter.click_button_yes()
        order_scooter.click_button_view_status()
        order_scooter.check_number_order()

    @allure.title("Проверка успешного заказа самоката через нижнюю кнопку 'Заказать'")
    @allure.description("""
        Тест проверяет полный процесс заказа самоката:
        1. Нажатие на нижнюю кнопку 'Заказать'
        2. Заполнение первой формы заказа (личные данные)
        3. Выбор станции метро
        4. Переход ко второй форме заказа
        5. Заполнение деталей аренды (дата, срок, цвет самоката, комментарий)
        6. Подтверждение заказа
        7. Проверка номера заказа
        """)
    def test_success_ful_order_second(self, driver):
        order_scooter = OrderScooter(driver)
        order_scooter.click_order_button_lower()
        order_scooter.fill_first_order_form(data.OrderScooterSecond.name, data.OrderScooterSecond.surname, data.OrderScooterSecond.address, data.OrderScooterSecond.telephone)
        order_scooter.choose_metro(data.OrderScooterSecond.station_name)
        order_scooter.click_button_further()
        order_scooter.fill_second_order_form(data.OrderScooterSecond.date, data.OrderScooterSecond.comment)
        order_scooter.choose_rental_period()
        order_scooter.choose_scooter_color()
        order_scooter.click_button_order()
        order_scooter.click_button_yes()
        order_scooter.click_button_view_status()
        order_scooter.check_number_order()