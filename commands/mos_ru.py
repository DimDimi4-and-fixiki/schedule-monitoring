from common.scrappers.mos_ru import MosRuScrapper
from common.utils import get_current_platform
from common.web_drivers.factories import chrome_driver_factory


def run_mos_ru_monitoring():
    driver = chrome_driver_factory.from_platform(platform=get_current_platform())
    scrapper = MosRuScrapper(driver)
    scrapper.fill_login_page()
