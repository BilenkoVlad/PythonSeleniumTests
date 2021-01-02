import pytest
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.add_remove_elements_page import add_remove_elements_page
from herokuApp.resources.TestData import browser


class Test_TC001_user_is_able_to_add_and_remove_items:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_add_remove_items(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link('Add/Remove Elements')

        self.add_remove_page = add_remove_elements_page(self.driver)
        self.add_remove_page.add_button_click()
        self.add_remove_page.delete_button_click()
        self.add_remove_page.add_button_click_10_times()
        self.add_remove_page.delete_button_click_10_times()
