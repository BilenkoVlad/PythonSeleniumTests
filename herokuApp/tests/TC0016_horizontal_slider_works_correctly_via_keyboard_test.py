import pytest

from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.horizontal_slider_page import horizontal_slider_page
from herokuApp.resources.TestData import browser


class Test_TC0016_horizontal_slider_works_correctly_via_keyboard:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_horizontal_slider_works_correctly_via_keyboard(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Horizontal Slider")

        self.horizontal_slider_page = horizontal_slider_page(self.driver)
        self.horizontal_slider_page.verify_default_content()
        self.horizontal_slider_page.move_slider_up_by_keyboard()
        self.horizontal_slider_page.move_slider_down_by_keyboard()
