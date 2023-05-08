import typing as t
from copy import deepcopy
from pathlib import Path

from selenium import webdriver
from selenium.webdriver import ChromeOptions

import config
from common.enums import Platform


class ChromeDriverFactory:
    DRIVERS_DIR = config.PROJECT_DIR / 'browsers_drivers' / 'chrome'
    PLATFORM_TO_DRIVER_PATH: t.Dict[Platform, Path] = {
        Platform.Mac: DRIVERS_DIR / 'mac' / 'chromedriver',
        Platform.Linux: ...,
    }

    @staticmethod
    def _add_options(options: ChromeOptions) -> ChromeOptions:
        options = deepcopy(options)

        options.add_argument('--disable-dev-shm-using')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')

        # Experimental options
        options.add_experimental_option('detach', True)
        options.add_argument(f'--remote-debugging-port={config.SELENIUM_REMOTE_DEBUGGING_PORT}')

        return options

    def from_platform(
        self, platform: t.Optional[Platform] = None, hidden: bool = config.HIDE_SELENIUM_BROWSER
    ) -> webdriver.Chrome:
        platform = platform or Platform.Linux
        options = self._add_options(ChromeOptions())

        if hidden:
            options.add_argument('--headless')

        return webdriver.Chrome(executable_path=self.PLATFORM_TO_DRIVER_PATH[platform], options=options)


chrome_driver_factory = ChromeDriverFactory()
