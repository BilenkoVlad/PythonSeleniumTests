import pytest
from herokuApp.main_folder.page_objects.disappearing_elements_page import disappearing_elements_page
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.resources.TestData import browser


class Test_TC006_verifying_that_hidden_item_can_be_shown_after_polling_the_page:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_verifying_that_hidden_item_can_be_shown_after_polling_the_page(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Disappearing Elements")

        self.disappearing_elements_page = disappearing_elements_page(self.driver)
        self.disappearing_elements_page.verify_default_content()
        self.disappearing_elements_page.wait_for_presence_of_hidden_element()
        self.disappearing_elements_page.wait_for_absence_of_hidden_element()
