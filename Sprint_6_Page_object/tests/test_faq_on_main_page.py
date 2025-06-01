from pages.main_page import MainPage
import allure
import pytest
from data.main_page_questions import FAQ_text_and_locators


class TestFAQOnMainPage:

    @allure.title("FAQ: проверка текста и ответа")
    @pytest.mark.parametrize("question_data", FAQ_text_and_locators)
    def test_faq_question_and_answer(self, browser, question_data):

        page = MainPage(browser)
        page.open()
        page.go_to_faq_menu()

        q_locator = question_data["question_locator"]
        a_locator = question_data["answer_locator"]
        q_text = question_data["question_text"]
        a_text = question_data["answer_text"]

        actual_q_text, actual_a_text = page.get_question_and_answer(q_locator, a_locator)

        assert actual_q_text == q_text, f"Wrong question text → {actual_q_text}"
        assert actual_a_text == a_text, f"Wrong answer text → {actual_a_text}"
