import pytest

from herokuApp.main_folder.page_objects.dropdown_page import dropdown_page
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.resources.TestData import browser


class Test_TC008_user_is_able_to_select_value_from_dropdown_list:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_select_value_from_dropdown_list(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Dropdown")

        self.dropdown_page = dropdown_page(self.driver)
        self.dropdown_page.verify_default_content()
        self.dropdown_page.select_option_from_dropdown("Option 1")
        self.dropdown_page.select_option_from_dropdown("Option 2")
        self.driver.refresh()
        self.dropdown_page.verify_default_content()
