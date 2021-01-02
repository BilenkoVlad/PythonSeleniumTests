from selenium.webdriver.common.by import By


class disappearing_elements_page:
    __header_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='example']/p")
    __buttons = (By.XPATH, "//ul//li")
    __hidden_button = (By.XPATH, "//ul//li//*[contains(text(), 'Gallery')]")
    __buttons_names = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]

    def __init__(self, driver):
        self.driver = driver

    def __header_page_text(self) -> str:
        return self.driver.find_element(*self.__header_page).text

    def __body_text(self) -> str:
        return self.driver.find_element(*self.__body).text

    def __hidden_button_element(self):
        return self.driver.find_element(*self.__hidden_button)

    def __buttons_elements(self) -> list:
        return self.driver.find_elements(*self.__buttons)

    def verify_default_content(self):
        assert self.__header_page_text() == "Disappearing Elements"
        assert self.__body_text() == \
               "This example demonstrates when elements on a page change by disappearing/reappearing on each page load."
        for i in range(len(self.__buttons_elements())):
            assert self.__buttons_elements()[i].is_displayed() == True
            assert self.__buttons_elements()[i].text == self.__buttons_names[i]

    def wait_for_presence_of_hidden_element(self):
        while self.__buttons_elements()[0].is_displayed():
            self.driver.refresh()
            if len(self.__buttons_elements()) == 5:
                assert self.__hidden_button_element().is_displayed() == True
                assert self.__hidden_button_element().text == self.__buttons_names[-1]
                break

    def wait_for_absence_of_hidden_element(self):
        while self.__buttons_elements()[0].is_displayed():
            self.driver.refresh()
            if len(self.__buttons_elements()) == 4:
                assert self.__buttons_elements()[len(self.__buttons_elements()) - 1].text == self.__buttons_names[-2]
                break
