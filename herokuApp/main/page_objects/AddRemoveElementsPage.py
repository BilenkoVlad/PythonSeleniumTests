from selenium.webdriver.common.by import By


class AddRemoveElementsPage:
    __addButton = (By.XPATH, "//button[@onclick='addElement()']")
    __deleteButtons = (By.XPATH, "//button[@onclick='deleteElement()']")

    def __init__(self, driver):
        self.driver = driver

    def addButtonIsDisplayed(self):
        assert self.driver.find_element(*self.__addButton).is_enabled() == True

    def addButtonClick(self):
        self.addButtonIsDisplayed()
        self.driver.find_element(*self.__addButton).click()

    def deleteButtonClick(self):
        self.driver.find_element(*self.__deleteButtons).click()

    def addButtonClick10Times(self):
        self.addButtonIsDisplayed()
        for i in range(10):
            self.driver.find_element(*self.__addButton).click()
            assert self.driver.find_elements(*self.__deleteButtons)[i].is_displayed()
        assert len(self.driver.find_elements(*self.__deleteButtons)) == 10

    def deleteButtonClick10Times(self):
        ind = len(self.driver.find_elements(*self.__deleteButtons)) - 1
        while ind >= 0:
            self.driver.find_elements(*self.__deleteButtons)[ind].click()
            assert len(self.driver.find_elements(*self.__deleteButtons)) == ind
            ind -= 1
        assert len(self.driver.find_elements(*self.__deleteButtons)) == 0
