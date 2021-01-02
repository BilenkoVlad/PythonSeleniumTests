import pytest
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.checkboxes_page import checkboxes_page
from herokuApp.resources.TestData import browser


class Test_TC004_user_is_able_to_check_and_uncheck_checkboxes:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_check_and_uncheck_checkboxes(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Checkboxes")

        self.checkboxes_page = checkboxes_page(self.driver)
        self.checkboxes_page.verify_default_content()
        self.checkboxes_page.select_first_checkbox()
        self.checkboxes_page.unselect_checkboxes()
        self.checkboxes_page.select_first_checkbox()
        self.driver.refresh()
        self.checkboxes_page.verify_default_content()
