import unittest

from selenium import webdriver
from main.page_objects.HomePage import HomePage
from main.page_objects.AddRemoveElementsPage import AddRemoveElementsPage


class TC001_UserIsAbleToAddAndRemoveItems(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class TC001_UserIsAbleToAddAndRemoveItemsTest(TC001_UserIsAbleToAddAndRemoveItems):
    def setUp(self):
        super().setUp()

    def test_home_page_loaded_successfully(self):
        self.homePage = HomePage(self.driver)
        self.homePage.clickOnLink('Add/Remove Elements')

        self.add_remove_page = AddRemoveElementsPage(self.driver)
        self.add_remove_page.addButtonClick()
        self.add_remove_page.deleteButtonClick()
        self.add_remove_page.addButtonClick10Times()
        self.add_remove_page.deleteButtonClick10Times()
