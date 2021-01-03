from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class dynamic_controls_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h4")
    __body = (By.XPATH, "//div[@class='example']/p")
    __remove_button = (By.XPATH, "//button[text()='Remove']")
    __add_button = (By.XPATH, "//button[text()='Add']")
    __message = (By.XPATH, "//p[@id='message']")
    __input_loading = (By.XPATH, "//form[@id='input-example']//div[@id='loading']")
    __checkbox_loading = (By.XPATH, "//form[@id='checkbox-example']//div[@id='loading']")
    __enable_button = (By.XPATH, "//button[text()='Enable']")
    __disable_button = (By.XPATH, "//button[text()='Disable']")
    __checkbox = (By.XPATH, "//input[@type='checkbox']")
    __text_field = (By.XPATH, "//input[@type='text']")
    __expected_headers = ["Dynamic Controls", "Remove/add", "Enable/disable"]

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_elements(self):
        return self.driver.find_elements(*self.__headers_page)

    def __body_text(self):
        return self.driver.find_element(*self.__body).text

    def __remove_button_element(self):
        return self.driver.find_element(*self.__remove_button)

    def __add_button_element(self):
        return self.driver.find_element(*self.__add_button)

    def __message_text(self, option):
        return self.driver.find_element(*self.__message).text if option == "text" \
            else self.driver.find_element(*self.__message)

    def __input_loading_element(self):
        return self.driver.find_element(*self.__input_loading)

    def __checkbox_loading_elements(self):
        return self.driver.find_elements(*self.__checkbox_loading)

    def __enable_button_element(self):
        return self.driver.find_element(*self.__enable_button)

    def __disable_button_element(self):
        return self.driver.find_element(*self.__disable_button)

    def __checkbox_element(self):
        return self.driver.find_element(*self.__checkbox)

    def __text_field_element(self):
        return self.driver.find_element(*self.__text_field)

    def __wait_for_message(self):
        web_driver_wait = WebDriverWait(self.driver, 5)
        web_driver_wait.until(EC.presence_of_element_located(self.__message))

    def __is_element_present(self, element):
        try:
            self.driver.find_element(*element)
            return True
        except NoSuchElementException:
            return False

    def verify_default_content(self):
        for i in range(len(self.__headers_page_elements())):
            assert self.__headers_page_elements()[i].text == self.__expected_headers[i]
        assert self.__body_text() == "This example demonstrates when elements " \
                                     "(e.g., checkbox, input field, etc.) are changed asynchronously."
        assert self.__checkbox_element().is_selected() == False
        assert self.__remove_button_element().is_displayed() and self.__remove_button_element().is_enabled() == True
        assert self.__text_field_element().is_enabled() == False
        assert self.__enable_button_element().is_displayed() and self.__enable_button_element().is_enabled() == True

    def select_checkbox(self):
        self.__checkbox_element().click()
        assert self.__checkbox_element().is_selected() == True

    def click_on_remove_button(self):
        self.__remove_button_element().click()
        assert self.__checkbox_loading_elements()[0].is_displayed()
        self.__wait_for_message()
        assert self.__message_text("element").is_displayed()
        assert self.__message_text("text") == "It's gone!"
        assert self.__is_element_present(self.__checkbox) == False
        assert self.__add_button_element().is_displayed() and self.__add_button_element().is_enabled() == True

    def click_on_add_button(self):
        self.__add_button_element().click()
        assert self.__checkbox_loading_elements()[0].is_displayed() == True
        self.__wait_for_message()
        assert self.__message_text("element").is_displayed()
        assert self.__message_text("text") == "It's back!"
        assert self.__checkbox_element().is_displayed() == True
        assert self.__checkbox_element().is_selected() == False

    def click_on_enable_button(self):
        self.__enable_button_element().click()
        assert self.__input_loading_element().is_displayed() == True
        self.__wait_for_message()
        assert self.__message_text("element").is_displayed() == True
        assert self.__message_text("text") == "It's enabled!"
        assert self.__text_field_element().is_enabled() == True
        assert self.__disable_button_element().is_enabled() and self.__disable_button_element().is_displayed() == True

    def enter_text_into_field(self, text):
        self.__text_field_element().send_keys(text)
        assert self.__text_field_element().get_attribute("value") == text

    def click_on_disable_button(self):
        self.enter_text_into_field("Test text is automatically added")
        self.__disable_button_element().click()
        assert self.__input_loading_element().is_displayed() == True
        self.__wait_for_message()
        assert self.__message_text("element").is_displayed() == True
        assert self.__message_text("text") == "It's disabled!"
        assert self.__text_field_element().is_enabled() == False
        assert self.__enable_button_element().is_enabled() and self.__enable_button_element().is_displayed() == True
        assert self.__text_field_element().get_attribute("value") == "Test text is automatically added"
