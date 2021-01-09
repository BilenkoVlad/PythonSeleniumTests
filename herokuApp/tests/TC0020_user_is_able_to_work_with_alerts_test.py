import pytest

from herokuApp.main_folder.page_objects.home_page import home_page
from herokuApp.main_folder.page_objects.javascript_alerts_page import javascript_alerts_page
from herokuApp.resources.TestData import browser


class Test_TC0020_user_is_able_to_work_with_alerts:
    @pytest.fixture()
    def browser_init(self):
        self.driver = browser("chrome")
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_user_is_able_to_work_with_alerts(self, browser_init):
        self.home_page = home_page(self.driver)
        self.home_page.click_on_link("JavaScript Alerts")

        self.javascript_alerts_page = javascript_alerts_page(self.driver)
        self.javascript_alerts_page.verify_default_content()
        self.javascript_alerts_page.click_on_js_alert()

        self.javascript_alerts_page.click_on_js_confirm("OK")
        self.javascript_alerts_page.click_on_js_confirm("Cancel")

        self.javascript_alerts_page.click_on_js_prompt_with_text("OK", "Test text with !@#$%^&*()")
        self.javascript_alerts_page.click_on_js_prompt_with_text("Cancel", "Test text with !@#$%^&*()")

        self.javascript_alerts_page.click_on_js_prompt_without_text("OK")
        self.javascript_alerts_page.click_on_js_prompt_without_text("Cancel")
