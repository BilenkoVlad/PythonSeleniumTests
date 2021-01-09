import pytest

from herokuApp.main_folder.page_objects.frames_page import frames_page
from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.nested_frames_page import nested_frames_page
from herokuApp.resources.TestData import browser


class Test_TC0015_text_in_the_nested_frames_is_shown_correctly:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    @pytest.mark.xfail
    def test_text_in_the_nested_frames_is_shown_correctly(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Frames")

        self.frames_page = frames_page(self.driver)
        self.frames_page.verify_default_content()
        self.frames_page.click_nested_frames_link()

        self.nested_frames_page = nested_frames_page(self.driver)
        self.nested_frames_page.check_names()

