import pytest

from herokuApp.main_folder.page_objects.dynamic_loading_page import dynamic_loading_page
from herokuApp.main_folder.page_objects.example1_hidden_elements_page import example1_hidden_elements_page
from herokuApp.main_folder.page_objects.example2_element_rendered import example2_element_rendered
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.resources.TestData import browser


class Test_TC0010_verify_that_elements_dynamically_loaded:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_verify_that_elements_dynamically_loaded(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Dynamic Loading")

        self.dynamic_loading_page = dynamic_loading_page(self.driver)
        self.dynamic_loading_page.verify_default_content()
        self.dynamic_loading_page.click_on_first_link()

        self.example1_hidden_elements_page = example1_hidden_elements_page(self.driver)
        self.example1_hidden_elements_page.verify_default_content()
        self.example1_hidden_elements_page.click_start_button()
        self.driver.back()

        self.dynamic_loading_page.click_on_second_link()

        self.example2_element_rendered = example2_element_rendered(self.driver)
        self.example2_element_rendered.verify_default_content()
        self.example2_element_rendered.click_start_button()
