import pytest

from herokuApp.main_folder.page_objects.entry_ad_page import entry_ad_page
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.resources.TestData import browser


class Test_TC0011_user_is_able_to_see_modal_window_and_can_close_it:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_see_modal_window_and_can_close_it(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Entry Ad")

        self.entry_ad_page = entry_ad_page(self.driver)
        self.entry_ad_page.verify_default_content_modal_window()
        self.entry_ad_page.click_close_button()
        self.entry_ad_page.verify_default_content()
        self.entry_ad_page.click_on_here_link()
        self.entry_ad_page.verify_default_content_modal_window()
        self.entry_ad_page.click_close_button()
        self.entry_ad_page.refresh_page()