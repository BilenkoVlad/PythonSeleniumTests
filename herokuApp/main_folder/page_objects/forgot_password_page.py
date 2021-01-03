from selenium.webdriver.common.by import By
from herokuApp.resources.TestData import email_generator


class forgot_password_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h2")
    __field_label = (By.XPATH, "//label[@for='email']")
    __email_field = (By.XPATH, "//input[@id='email']")
    __retrieve_password_button = (By.XPATH, "//button[@id='form_submit']")
    __button_name = (By.XPATH, "//button[@id='form_submit']/i")
    __sent_notification = (By.XPATH, "//div[@id='content']")
    email = email_generator()

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __field_label_element(self):
        return self.driver.find_element(*self.__field_label)

    def __email_field_element(self):
        return self.driver.find_element(*self.__email_field)

    def __retrieve_password_button_element(self):
        return self.driver.find_element(*self.__retrieve_password_button)

    def __button_name_text(self):
        return self.driver.find_element(*self.__button_name).text

    def __send_notification_element(self):
        return self.driver.find_element(*self.__sent_notification)

    def verify_default_content(self):
        assert self.__headers_page_text() == "Forgot Password"
        assert self.__field_label_element().text == "E-mail"
        assert self.__email_field_element().is_displayed() and self.__email_field_element().is_enabled() == True
        assert self.__button_name_text() == "Retrieve password"
        assert self.__retrieve_password_button_element().is_displayed() and \
               self.__retrieve_password_button_element().is_enabled() == True

    def enter_email_for_restore_password(self):
        self.__email_field_element().send_keys(self.email)
        self.__retrieve_password_button_element().click()
        assert self.__send_notification_element().is_displayed() == True
        assert self.__send_notification_element().text.strip() == "Your e-mail's been sent!"
