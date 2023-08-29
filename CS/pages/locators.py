from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGO_LOCATOR = (By.XPATH, '//img[@src="/images/katami.png"]')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[@id="bx_basketFKauiI"]/div/div[1]/a[1]')
    INPUT_LOGIN_LOCATOR = (By.XPATH, '//input[contains(@name, "USER_LOGIN")]')
    INPUT_PASSWORD_LOCATOR = (By.XPATH, '//input[contains(@name, "USER_PASSWORD")]')
    SIGN_IN_BUTTON_LOCATOR = (By.XPATH, '//input[contains(@class, "btn btn-primary")]')
    INVALID_AUTH_MESSAGE = (By.XPATH, '//div[contains(@class, "alert alert-danger")]')
    VALID_AUTH_MESSAGE = (By.XPATH, '//a[contains(@class, "basket-line-block-icon-profile") and .="Георгий Гагарин"]')
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//*[@id="bx_basketFKauiI"]/div/div[1]/a[2]')
    REGISTRATION_BUTTON_LOCATOR = (By.XPATH, '//*[@id="bx_basketFKauiI"]/div/div[1]/a[2]')

