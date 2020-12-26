from selenium.webdriver.common.by import By
from resources.TestData import TestData


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.BASE_URL)

    def clickOnLink(self, name):
        self.driver.find_element(By.XPATH, f"//*[contains(text(), '{name}')]").click()
