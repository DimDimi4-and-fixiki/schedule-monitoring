from pathlib import Path

from selenium import webdriver


class ChromeDriver:
    def __init__(self, driver_path: Path):
        self.driver = webdriver.Chrome(driver_path.as_posix())
