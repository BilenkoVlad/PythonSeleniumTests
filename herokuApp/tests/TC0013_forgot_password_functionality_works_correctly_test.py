import pytest

from herokuApp.main_folder.page_objects.forgot_password_page import forgot_password_page
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.mailinator_page import mailinator_page
from herokuApp.resources.TestData import browser


class Test_TC0013_forgot_password_functionality_works_correctly:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_forgot_password_functionality_works_correctly(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Forgot Password")

        self.forgot_password_page = forgot_password_page(self.driver)
        self.forgot_password_page.verify_default_content()
        self.forgot_password_page.enter_email_for_restore_password()

        self.mailinator_page = mailinator_page(self.driver)
        self.mailinator_page.go_to_email_site()
        self.mailinator_page.enter_email(forgot_password_page.email)
        self.mailinator_page.click_on_received_email()
