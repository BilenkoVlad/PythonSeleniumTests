import pytest

from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.multiple_windows_page import multiple_windows_page
from herokuApp.main_folder.page_objects.new_window_page import new_window_page
from herokuApp.resources.TestData import browser


class Test_TC0022_user_is_able_to_open_and_navigate_to_the_new_window:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_open_and_navigate_to_the_new_window(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Multiple Windows")

        self.multiple_windows_page = multiple_windows_page(self.driver)
        self.multiple_windows_page.verify_default_content()
        self.multiple_windows_page.click_on_link()

        self.new_window_page = new_window_page(self.driver)
        self.new_window_page.verify_default_content()
