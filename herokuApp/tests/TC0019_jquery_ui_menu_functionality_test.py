import pytest

from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.jquery_page import jquery_page
from herokuApp.main_folder.page_objects.jquery_ui_menu_page import jquery_ui_menu_page
from herokuApp.resources.TestData import browser


class Test_TC0019_jquery_ui_menu_functionality:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_jquery_ui_menu_functionality(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("JQuery UI Menus")

        self.jquery_ui_menu_page = jquery_ui_menu_page(self.driver)
        self.jquery_ui_menu_page.verify_default_content()
        self.jquery_ui_menu_page.click_on_jquery_link()

        self.jquery_page = jquery_page(self.driver)
        self.jquery_page.verify_jquery_page()

        self.driver.back()
        self.jquery_ui_menu_page.verify_default_content()
        self.jquery_ui_menu_page.download_all_files()
        self.jquery_ui_menu_page.click_on_menu_option("Back to JQuery UI")
