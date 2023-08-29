from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .pages.main_page import MainPage


class TestExample:

    def test_home_page_check(self, browser):
        # Данные
        page = MainPage(browser)

        # Подготовка
        page.open()

        # Проверка
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//img[@src="/images/katami.png"]')))
        page.should_be_main_page()

    def test_entering_incorrect_data_for_authorization(self, browser):
        # Данные
        incorrect_name = "test"
        incorrect_password = "test"
        page = MainPage(browser)

        # Подготовка
        page.open()
        page.click_on_login_button()
        page.authorization_with_incorrect_data(incorrect_name, incorrect_password)

        # Проверка
        page.check_for_invalid_authorization_message()

    def test_entering_with_correct_data_for_authorization(self, browser):
        # Данные
        name = "test3"
        password = "Fabrika4"
        page = MainPage(browser)

        # Подготовка
        page.open()
        page.click_on_login_button()
        page.authorization_with_correct_data(name, password)
        page.check_for_valid_authorization_message()
        page.click_on_logout_button()

        # Проверка
        page.check_that_logout_has_occurred()






