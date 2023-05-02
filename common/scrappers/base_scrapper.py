import typing as t

from selenium import webdriver

import config


class BaseScrapper:
    def __init__(self, driver: webdriver.Chrome, resource_url: str):
        self.driver = driver
        self.url = resource_url

    def load_page(self, url=None) -> None:
        url = url or self.url
        self.driver.get(url)

    def end_sessions(self) -> None:
        self.driver.quit()


class MosRuScrapper(BaseScrapper):
    def __init__(self, driver: webdriver.Chrome, resource_url: t.Optional[str] = None):
        url = resource_url or config.MOS_RU_URL
        super().__init__(driver=driver, resource_url=url)
