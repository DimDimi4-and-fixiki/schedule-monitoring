import typing as t

import selenium.webdriver
from selenium.webdriver.common.by import By

import config
from common.decorators import sleep_after


class BasePage:
    def __init__(self, driver: selenium.webdriver.Remote, url: str):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)


class MosRuLoginPage(BasePage):
    def __init__(
        self,
        driver: selenium.webdriver.Remote,
        url: str = config.MOS_RU_URL,
        login: t.Optional[str] = None,
        password: t.Optional[str] = None,
    ):

        super().__init__(driver, url)
        self.login = login or config.MOS_RU_LOGIN
        self.password = password or config.MOS_RU_PASSWORD
        self.open()

    @sleep_after(seconds=config.MOS_RU_LOGIN_FORM_FILL_DELAY)
    def fill_login(self):
        login_field = self.driver.find_element(By.ID, 'login')
        login_field.send_keys(self.login)

    @sleep_after(seconds=config.MOS_RU_LOGIN_FORM_FILL_DELAY)
    def fill_password(self):
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys(self.password)

    @sleep_after(seconds=config.MOS_RU_LOGIN_FORM_FILL_DELAY)
    def submit_login_form(self):
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'form-login__submit')
        submit_btn.click()
