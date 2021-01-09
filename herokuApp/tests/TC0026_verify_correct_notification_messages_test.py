import pytest

from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.notification_messages_page import notification_messages_page
from herokuApp.resources.TestData import browser


class Test_TC0026_verify_correct_notification_messages:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_verify_correct_notification_messages(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("Notification Messages")

        self.notification_messages_page = notification_messages_page(self.driver)
        self.notification_messages_page.verify_default_content()
