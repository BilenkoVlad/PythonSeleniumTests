from selenium.webdriver.common.by import By


class jquery_page:
    __page_title = (By.XPATH, "//h1[@class='entry-title']")
    __jquery_menu_url = "https://api.jqueryui.com/menu/"

    def __init__(self, driver):
        self.driver = driver

    def __page_title_text(self):
        return self.driver.find_element(*self.__page_title).text

    def verify_jquery_page(self):
        assert self.__page_title_text() == "Menu Widget"
        assert self.driver.current_url == self.__jquery_menu_url
