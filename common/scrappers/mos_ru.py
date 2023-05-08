import typing as t

from selenium import webdriver

import config
from common.decorators import sleep_after
from common.scrappers.base_scrapper import ChromeBaseScrapper
from common.scrappers.entities import MosRuLoginPage


class MosRuScrapper(ChromeBaseScrapper):
    @sleep_after(seconds=5)
    def __init__(self, driver: webdriver.Chrome, resource_url: t.Optional[str] = None):
        url = resource_url or config.MOS_RU_URL
        super().__init__(driver=driver, resource_url=url)

    @sleep_after(seconds=config.MOS_RU_LOGIN_FORM_FILL_DELAY)
    def fill_login_page(self):
        page = MosRuLoginPage(driver=self.driver)
        page.fill_login()
        page.fill_password()
        page.submit_login_form()
