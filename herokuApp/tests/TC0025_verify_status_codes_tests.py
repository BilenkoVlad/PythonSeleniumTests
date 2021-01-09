import pytest

from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.status_codes_pages import status_codes_pages
from herokuApp.resources.TestData import browser


class Test_TC0025_verify_status_codes:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_verify_status_codes(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Status Codes")

        self.status_codes_pages = status_codes_pages(self.driver)
        self.status_codes_pages.verify_default_content()
        self.status_codes_pages.click_on_200_code()
        self.driver.back()
        self.status_codes_pages.click_on_301_code()
        self.driver.back()
        self.status_codes_pages.click_on_404_code()
        self.driver.back()
        self.status_codes_pages.click_on_500_code()
