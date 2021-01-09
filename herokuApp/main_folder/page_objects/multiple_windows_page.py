from selenium.webdriver.common.by import By


class multiple_windows_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __click_here_link = (By.XPATH, "//div[@class='example']/a")

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __click_here_link_element(self):
        return self.driver.find_element(*self.__click_here_link)

    def __switch_to_new_window(self):
        self.driver.switch_to_window((self.driver.window_handles[-1]))

    def verify_default_content(self):
        assert self.__headers_page_text() == "Opening a new window"
        assert self.__click_here_link_element().text == "Click Here"
        assert self.__click_here_link_element().is_displayed() and self.__click_here_link_element().is_enabled() == True

    def click_on_link(self):
        self.__click_here_link_element().click()
        self.__switch_to_new_window()
