from selenium.common.exceptions import NoSuchElementException

from .locators import BasePageLocators
import time

class BasePage():
    def __init__(self, browser, url, timeout=20):
        self.page_url = ""
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10

    site_url = "https://katamiwear.com/"


    def should_be_main_page(self):
        assert self.is_element_present(*BasePageLocators.LOGO_LOCATOR), "Главный логотип не найден,"

    def click_on_login_button(self):
        time.sleep(2)
        self.browser.implicitly_wait(10)
        link = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON_LOCATOR)
        link.click()


    def authorization_with_incorrect_data(self, incorrect_name, incorrect_password):
        self.browser.implicitly_wait(10)
        self.browser.find_element(*BasePageLocators.INPUT_LOGIN_LOCATOR).send_keys(incorrect_name)
        self.browser.find_element(*BasePageLocators.INPUT_PASSWORD_LOCATOR).send_keys(incorrect_password)
        link = self.browser.find_element(*BasePageLocators.SIGN_IN_BUTTON_LOCATOR)
        link.click()
        self.browser.implicitly_wait(10)

    def check_for_invalid_authorization_message(self):
        assert self.is_element_present(*BasePageLocators.INVALID_AUTH_MESSAGE), "Произошел вход по некорректным кредам"

    def authorization_with_correct_data(self, name, password):
        self.browser.implicitly_wait(10)
        self.browser.find_element(*BasePageLocators.INPUT_LOGIN_LOCATOR).send_keys(name)
        self.browser.find_element(*BasePageLocators.INPUT_PASSWORD_LOCATOR).send_keys(password)
        link = self.browser.find_element(*BasePageLocators.SIGN_IN_BUTTON_LOCATOR)
        link.click()
        self.browser.implicitly_wait(10)

    def check_for_valid_authorization_message(self):
        assert self.is_element_present(*BasePageLocators.VALID_AUTH_MESSAGE), "Не поизошел вход по корректным кредам"

    def click_on_logout_button(self):
        self.browser.implicitly_wait(20)
        link = self.browser.find_element(*BasePageLocators.LOGOUT_BUTTON_LOCATOR)
        link.click()
        self.browser.implicitly_wait(10)

    def check_that_logout_has_occurred(self):
        assert self.is_element_present(*BasePageLocators.REGISTRATION_BUTTON_LOCATOR), "Не поизошел выход пользователя"

    def open(self):
        self.browser.get(self.url)

    # реализуем метод is_element_present, в котором будем перехватывать исключение
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True