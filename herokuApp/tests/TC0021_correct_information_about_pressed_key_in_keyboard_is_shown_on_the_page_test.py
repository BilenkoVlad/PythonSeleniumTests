import pytest

from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.key_presses_page import key_presses_page
from herokuApp.resources.TestData import browser


class Test_TC0021_correct_information_about_pressed_key_in_keyboard_is_shown_on_the_page:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    @pytest.mark.parametrize("keys, chars",
                             [
                                 (True, False),
                                 (False, True)
                             ])
    def test_correct_information_about_pressed_key_in_keyboard_is_shown_on_the_page(self, browser_init, keys, chars):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Key Presses")

        self.key_presses_page = key_presses_page(self.driver)
        self.key_presses_page.verify_default_content()
        if keys:
            self.key_presses_page.press_keys_on_page()
        else:
            self.key_presses_page.press_chars_on_page()
