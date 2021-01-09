import pytest

from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.hovers_page import hovers_page
from herokuApp.resources.TestData import browser


class Test_TC0017_user_is_able_to_see_additional_information_after_hover_the_mouse_onto_avatar:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_see_additional_information_after_hover_the_mouse_onto_avatar(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Hovers")

        self.hovers_page = hovers_page(self.driver)
        self.hovers_page.verify_default_content()
        self.hovers_page.hover_each_avatar()
