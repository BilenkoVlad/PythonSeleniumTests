import pytest

from herokuApp.main_folder.page_objects.file_download_page import file_download_page
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.resources.TestData import browser


class Test_TC0012_user_is_able_to_download_files:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_download_files(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("File Download")

        self.file_download_page = file_download_page(self.driver)
        self.file_download_page.verify_default_content()
        self.file_download_page.download_files()
