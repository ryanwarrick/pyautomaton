from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    submit_button = (By.ID, "Logon")
    login_page_identifier = (By.CLASS_NAME, "login-body")


class InternalPageLocators:
    internal_page_identifier = (By.ID, 'top-nav')
    score_text = (
        By.XPATH,
        '//*[@id = "__render-farm"]//*[@class = "credit-health"]/div[1]//*[@class = "section-content"]/div[1]/div[1]/div[1]/div[1]//*[name() = "svg"]/*[name() = "text"][position() = (last() - 1)]'
    )
