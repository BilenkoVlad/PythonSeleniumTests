from selenium.webdriver.common.by import By


class add_remove_elements_page:
    __add_button = (By.XPATH, "//button[@onclick='addElement()']")
    __delete_buttons = (By.XPATH, "//button[@onclick='deleteElement()']")

    def __init__(self, driver):
        self.driver = driver

    def add_button_is_displayed(self):
        assert self.driver.find_element(*self.__add_button).is_enabled() == True

    def add_button_click(self):
        self.add_button_is_displayed()
        self.driver.find_element(*self.__add_button).click()

    def delete_button_click(self):
        self.driver.find_element(*self.__delete_buttons).click()

    def add_button_click_10_times(self):
        self.add_button_is_displayed()
        for i in range(10):
            self.driver.find_element(*self.__add_button).click()
            assert self.driver.find_elements(*self.__delete_buttons)[i].is_displayed()
        assert len(self.driver.find_elements(*self.__delete_buttons)) == 10

    def delete_button_click_10_times(self):
        ind = len(self.driver.find_elements(*self.__delete_buttons)) - 1
        while ind >= 0:
            self.driver.find_elements(*self.__delete_buttons)[ind].click()
            assert len(self.driver.find_elements(*self.__delete_buttons)) == ind
            ind -= 1
        assert len(self.driver.find_elements(*self.__delete_buttons)) == 0
