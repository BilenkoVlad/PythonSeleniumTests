from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class mailinator_page:
    __enter_email_field = (By.XPATH, "//input[@id='addOverlay']")
    __go_button = (By.XPATH, "//button[@id='go-to-public']")
    __email_message = (By.XPATH, "//tr[@class='even pointer ng-scope']")

    def __init__(self, driver):
        self.driver = driver

    def __enter_email_field_element(self):
        return self.driver.find_element(*self.__enter_email_field)

    def __go_button_element(self):
        return self.driver.find_element(*self.__go_button)

    def __email_message_list(self):
        return self.driver.find_elements(*self.__email_message)

    def go_to_email_site(self):
        self.driver.get("https://www.mailinator.com")

    def enter_email(self, email):
        self.__enter_email_field_element().send_keys(email)
        self.__go_button_element().click()

    def click_on_received_email(self):
        web_driver_wat = WebDriverWait(self.driver, 5)
        web_driver_wat.until(EC.visibility_of_element_located(self.__email_message))
        assert self.__email_message_list()[0].is_displayed() == True
