import allure
from page_object.check_base_page import BasePage
from Locators.main_page_locators import MainPageLocators

class QuestionAnswer(BasePage):

    @allure.step("Нажать на вопрос с индексом {index}")
    def click_question(self, index):
        locator = MainPageLocators.fag_questions_items[index]
        self.wait_for_element(MainPageLocators.COOKIE)
        self.click_on_element(MainPageLocators.COOKIE)
        self.scroll_to_element(locator)
        self.wait_for_element(locator)
        self.click_on_element(locator)

    @allure.step("Получить текст ответа для вопроса {index}")
    def get_answer_text(self, index):
        locator = MainPageLocators.faq_answers_items[index]
        return self.get_text_on_element(locator)

