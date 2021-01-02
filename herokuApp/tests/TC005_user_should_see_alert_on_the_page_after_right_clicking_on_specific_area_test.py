import pytest
from herokuApp.main_folder.page_objects.context_menu_page import context_menu_page
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.resources.TestData import browser


class Test_TC005_user_should_see_alert_on_the_page_after_right_clicking_on_specific_area:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_should_see_alert_on_the_page_after_right_clicking_on_specific_area(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Context Menu")

        self.context_menu_page = context_menu_page(self.driver)
        self.context_menu_page.verify_default_content()
        self.context_menu_page.left_click_on_box()
        self.context_menu_page.right_click_out_box()
        self.context_menu_page.right_click_on_box()
