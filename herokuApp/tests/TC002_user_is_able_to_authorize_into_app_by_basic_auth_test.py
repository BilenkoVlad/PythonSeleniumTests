import pytest
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.basic_auth_page import basic_auth_page
from herokuApp.resources.TestData import browser


class Test_TC002_user_is_able_to_authorize_into_app_by_basic_auth:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    @pytest.mark.parametrize("user_name, user_password, valid",
                             [
                                 ("admin", "admin", "Correct"),
                                 ("incorrect", "incorrect", "Incorrect")
                             ])
    def test_user_is_able_to_authorize(self, browser_init, user_name, user_password, valid):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link('Basic Auth')

        self.basic_auth_page = basic_auth_page(self.driver)
        self.basic_auth_page.basic_auth_with_credentials(user_name, user_password)
        if valid == "Correct":
            self.basic_auth_page.verify_page_text()
