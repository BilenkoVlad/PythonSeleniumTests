import pytest

from herokuApp.main_folder.page_objects.dynamic_controls_page import dynamic_controls_page
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.resources.TestData import browser


class Test_TC009_user_is_able_to_enable_disable_input_field_and_add_delete_checkbox:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_enable_disable_input_field_and_add_delete_checkbox(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Dynamic Controls")

        self.dynamic_controls_page = dynamic_controls_page(self.driver)
        self.dynamic_controls_page.verify_default_content()
        self.dynamic_controls_page.select_checkbox()
        self.dynamic_controls_page.click_on_remove_button()
        self.dynamic_controls_page.click_on_add_button()
        self.dynamic_controls_page.click_on_enable_button()
        self.dynamic_controls_page.click_on_disable_button()
        self.driver.refresh()
        self.dynamic_controls_page.verify_default_content()
