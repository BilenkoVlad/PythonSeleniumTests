from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class inputs_page:
    __headers_page = (By.XPATH, "//div[@class='large-6 small-12 columns large-centered']/h3")
    __body = (By.XPATH, "//div[@class='example']/p")
    __input_field = (By.XPATH, "//input")

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_text(self):
        return self.driver.find_element(*self.__body).text

    def __input_field_element(self):
        return self.driver.find_element(*self.__input_field)

    def verify_default_content(self):
        assert self.__headers_page_text() == "Inputs"
        assert self.__body_text() == "Number"
        assert self.__input_field_element().get_attribute("type") == "number"
        assert self.__input_field_element().is_displayed() and self.__input_field_element().is_enabled() == True

    def enter_chars(self):
        self.__input_field_element().send_keys("any test chars")
        self.__input_field_element().send_keys("eee")
        self.__input_field_element().clear()
        self.__input_field_element().send_keys("123")
        self.__input_field_element().clear()
        self.__input_field_element().send_keys("4561e4641")
        self.__input_field_element().clear()

    def enter_chars_via_arrows(self):
        self.__input_field_element().click()
        for i in range(50):
            self.__input_field_element().send_keys(Keys.ARROW_UP)
        self.__input_field_element().clear()
        for i in range(50):
            self.__input_field_element().send_keys(Keys.ARROW_DOWN)
