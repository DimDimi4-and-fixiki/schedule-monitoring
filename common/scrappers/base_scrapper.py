from selenium import webdriver


class ChromeBaseScrapper:
    def __init__(self, driver: webdriver.Chrome, resource_url: str):
        self.driver = driver
        self.url = resource_url

    def load_page(self, url=None) -> None:
        url = url or self.url
        self.driver.get(url)

    def end_sessions(self) -> None:
        self.driver.quit()
