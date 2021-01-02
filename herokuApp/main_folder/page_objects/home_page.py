from selenium.webdriver.common.by import By
from herokuApp.resources.TestData import TestData


class home_page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.BASE_URL)

    def click_on_link(self, name):
        self.driver.find_element(By.XPATH, f"//*[contains(text(), '{name}')]").click()
