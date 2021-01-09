import pytest

from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.sortable_data_tables_page import sortable_data_tables_page
from herokuApp.resources.TestData import browser


class Test_TC0023_user_is_able_to_sort_table_desc_and_asc:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_sort_table_desc_and_asc(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Sortable Data Tables")

        self.sortable_data_tables_page = sortable_data_tables_page(self.driver)
        self.sortable_data_tables_page.verify_default_content()
        self.sortable_data_tables_page.sort_table_by_each_header_asc()
        self.sortable_data_tables_page.sort_table_by_each_header_desc()
