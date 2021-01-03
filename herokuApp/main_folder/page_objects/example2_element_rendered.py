from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class example2_element_rendered:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='example']/h4")
    __start_button = (By.XPATH, "//div[@id='start']/button")
    __loader = (By.XPATH, "//div[@id='loading']")
    __hidden_text = (By.XPATH, "//div[@id='finish']/h4")

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_text(self):
        return self.driver.find_element(*self.__body).text

    def __start_button_element(self):
        return self.driver.find_element(*self.__start_button)

    def __loader_element(self):
        return self.driver.find_element(*self.__loader)

    def __hidden_text_text(self, option):
        return self.driver.find_element(*self.__hidden_text).text if option == "text" \
            else self.driver.find_element(*self.__hidden_text)

    def __wait_for_hidden_text(self):
        web_driver_wait = WebDriverWait(self.driver, 10)
        web_driver_wait.until(EC.presence_of_element_located(self.__hidden_text))

    def verify_default_content(self):
        assert self.__headers_page_text() == "Dynamically Loaded Page Elements"
        assert self.__body_text() == "Example 2: Element rendered after the fact"
        assert self.__start_button_element().is_displayed() and self.__start_button_element().is_enabled() == True

    def click_start_button(self):
        self.__start_button_element().click()
        assert self.__loader_element().text == "Loading..."
        assert self.__loader_element().is_displayed()
        self.__wait_for_hidden_text()
        assert self.__hidden_text_text("element").is_displayed()
        assert self.__hidden_text_text("text") == "Hello World!"
