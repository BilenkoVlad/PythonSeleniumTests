from selenium.webdriver.common.by import By


class new_window_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def verify_default_content(self):
        assert self.__headers_page_text() == "New Window"
