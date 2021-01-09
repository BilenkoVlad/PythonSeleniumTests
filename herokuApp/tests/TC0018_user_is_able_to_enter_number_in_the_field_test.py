import pytest

from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.inputs_page import inputs_page
from herokuApp.resources.TestData import browser


class Test_TC0018_user_is_able_to_enter_number_in_the_field:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_enter_number_in_the_field(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Inputs")

        self.inputs_page = inputs_page(self.driver)
        self.inputs_page.verify_default_content()
        self.inputs_page.enter_chars()
        self.inputs_page.enter_chars_via_arrows()
