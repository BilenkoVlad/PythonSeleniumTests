from selenium.webdriver.common.by import By


class checkboxes_page:
    __header_page = (By.XPATH, "//div[@class='example']/h3")
    __checkboxes = (By.XPATH, "//input[@type='checkbox']")

    def __init__(self, driver):
        self.driver = driver

    def verify_default_content(self):
        header_text: str = self.driver.find_element(*self.__header_page).text
        assert header_text == "Checkboxes"
        assert self.driver.find_elements(*self.__checkboxes)[0].is_selected() == False
        assert self.driver.find_elements(*self.__checkboxes)[1].is_selected() == True

    def select_first_checkbox(self):
        self.driver.find_elements(*self.__checkboxes)[0].click()
        assert self.driver.find_elements(*self.__checkboxes)[0].is_selected() == True

    def unselect_checkboxes(self):
        count_checkboxes = len(self.driver.find_elements(*self.__checkboxes))
        assert self.driver.find_elements(*self.__checkboxes)[0].is_selected() == True
        assert self.driver.find_elements(*self.__checkboxes)[1].is_selected() == True
        for i in range(count_checkboxes):
            self.driver.find_elements(*self.__checkboxes)[i].click()
            assert self.driver.find_elements(*self.__checkboxes)[i].is_selected() == False
