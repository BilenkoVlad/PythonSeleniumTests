import pytest

from herokuApp.main_folder.page_objects.form_authentication_page import form_authentication_page
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.resources.TestData import browser


class Test_TC0014_user_is_able_to_login:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_login(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Form Authentication")

        self.form_authentication_page = form_authentication_page(self.driver)
        self.form_authentication_page.verify_default_content()
        self.form_authentication_page.enter_invalid_credentials()
        self.form_authentication_page.enter_valid_credentials()
        self.form_authentication_page.click_logout_button()
