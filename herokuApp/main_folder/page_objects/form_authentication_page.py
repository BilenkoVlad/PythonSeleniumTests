from selenium.webdriver.common.by import By


class form_authentication_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h2")
    __body = (By.XPATH, "//div[@class='example']/h4")
    __credentials = (By.XPATH, "//div[@class='example']/h4/em")
    __username_label = (By.XPATH, "//label[@for='username']")
    __username_field = (By.XPATH, "//input[@name='username']")
    __password_label = (By.XPATH, "//label[@for='password']")
    __password_field = (By.XPATH, "//input[@name='password']")
    __login_button = (By.XPATH, "//button")
    __login_button_label = (By.XPATH, "//button/i")
    __message = (By.XPATH, "//div[@id='flash']")
    __logout_button = (By.XPATH, "//a[@class='button secondary radius']")
    __logout_button_label = (By.XPATH, "//a[@class='button secondary radius']/i")

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_text(self):
        return self.driver.find_element(*self.__body).text

    def __credentials_list(self):
        return self.driver.find_elements(*self.__credentials)

    def __username_label_text(self, option):
        return self.driver.find_element(*self.__username_label).text if option == "text" \
            else self.driver.find_element(*self.__username_label)

    def __password_label_text(self, option):
        return self.driver.find_element(*self.__password_label).text if option == "text" \
            else self.driver.find_element(*self.__password_label)

    def __login_button_label_text(self, option):
        return self.driver.find_element(*self.__login_button_label).text if option == "text" \
            else self.driver.find_element(*self.__login_button_label)

    def __logout_button_label_text(self, option):
        return self.driver.find_element(*self.__logout_button_label).text if option == "text" \
            else self.driver.find_element(*self.__logout_button_label)

    def __username_field_element(self):
        return self.driver.find_element(*self.__username_field)

    def __password_field_element(self):
        return self.driver.find_element(*self.__password_field)

    def __login_button_element(self):
        return self.driver.find_element(*self.__login_button)

    def __logout_button_element(self):
        return self.driver.find_element(*self.__logout_button)

    def __message_text(self, option):
        return self.driver.find_element(*self.__message).text if option == "text" \
            else self.driver.find_element(*self.__message)

    def verify_default_content(self):
        assert self.__headers_page_text() == "Login Page"
        assert self.__body_text() == "This is where you can log into the secure area. Enter tomsmith" \
                                     " for the username and SuperSecretPassword! for the password. If the " \
                                     "information is wrong you should see error messages."
        assert self.__username_label_text("text") == "Username"
        assert self.__username_field_element().is_enabled() and self.__username_field_element().is_displayed() == True
        assert self.__password_label_text("text") == "Password"
        assert self.__password_field_element().is_enabled() and self.__password_field_element().is_displayed() == True
        assert self.__login_button_label_text("text").strip() == "Login"
        assert self.__login_button_element().is_enabled() and self.__login_button_element().is_displayed() == True

    def enter_invalid_credentials(self):
        self.__username_field_element().send_keys("invalidUsername")
        self.__password_field_element().send_keys("invalidPassword")
        self.__login_button_element().click()
        assert self.__message_text("element").is_displayed() == True
        assert self.__message_text("text").strip() == "Your username is invalid!\n×"

    def enter_valid_credentials(self):
        self.__username_field_element().send_keys(self.__credentials_list()[0].text)
        self.__password_field_element().send_keys(self.__credentials_list()[1].text)
        self.__login_button_element().click()
        assert self.__message_text("element").is_displayed() == True
        assert self.__message_text("text").strip() == "You logged into a secure area!\n×"
        assert self.__headers_page_text().strip() == "Secure Area"
        assert self.__body_text() == "Welcome to the Secure Area. When you are done click logout below."
        assert self.__logout_button_label_text("text").strip() == "Logout"
        assert self.__logout_button_element().is_enabled() and self.__logout_button_element().is_displayed() == True

    def click_logout_button(self):
        self.__logout_button_element().click()
        assert self.__message_text("element").is_displayed() == True
        assert self.__message_text("text").strip() == "You logged out of the secure area!\n×"
        self.verify_default_content()
