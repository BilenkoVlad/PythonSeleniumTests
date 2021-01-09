from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class jquery_ui_menu_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='description']/p")
    __jQuery_link = (By.XPATH, "//div[@class='description']/p/a")
    __menu = (By.XPATH, "//div[@class='description']/ul[@id='menu']")
    __disabled_option = (By.XPATH, "//div[@class='description']/ul[@id='menu']/li[@id='ui-id-1']")
    __enabled_option = (By.XPATH, "//div[@class='description']/ul[@id='menu']/li[@id='ui-id-3']")
    __enable_expanded_menu = (By.XPATH, "//*[@id='ui-id-3']/ul")
    __download_expanded_menu = (By.XPATH, "//*[@id='ui-id-4']/ul")

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_texts(self):
        return self.driver.find_elements(*self.__body)

    def __menu_element(self):
        return self.driver.find_element(*self.__menu)

    def __disabled_option_element(self):
        return self.driver.find_element(*self.__disabled_option)

    def __jQuery_link_element(self):
        return self.driver.find_element(*self.__jQuery_link)

    def __enabled_option_element(self):
        return self.driver.find_element(*self.__enabled_option)

    def __enable_expanded_menu_element(self):
        return self.driver.find_element(*self.__enable_expanded_menu)

    def __download_expanded_menu_element(self):
        return self.driver.find_element(*self.__download_expanded_menu)

    def __options(self, option):
        needed_option = (By.XPATH, f"//a[text()='{option}']")
        return self.driver.find_element(*needed_option)

    def __wait_for_element(self, element):
        web_driver_wait = WebDriverWait(self.driver, 5)
        web_driver_wait.until(EC.visibility_of(element))
        assert element.is_displayed() == True

    def __move_to_element(self, element_to_move, element_to_wait):
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_move).release().perform()
        self.__wait_for_element(element_to_wait)

    def verify_default_content(self):
        assert self.__headers_page_text() == "JQueryUI - Menu"
        assert self.__body_texts()[0].text.strip() == "JQuery UI Menus are a nice UI element from a user " \
                                                      "perspective, but poses an interesting automation challenge " \
                                                      "since it requires mouse operations and synchronization " \
                                                      "between them."
        assert self.__body_texts()[1].text.strip() == "Another 'fun' aspect is that the visibility of elements " \
                                                      "is actually not in the html itself, but done magically by " \
                                                      "JQuery so you cannot trust exactly what the html is telling " \
                                                      "you. A user cannot fire click events at certain UI elements, " \
                                                      "but you might -- if you have a big enough hammer to hit it with."
        assert self.__menu_element().is_displayed() == True
        assert self.__disabled_option_element().is_enabled() == True
        assert self.__enabled_option_element().is_enabled() == True

        self.__move_to_element(self.__enabled_option_element(), self.__enable_expanded_menu_element())
        assert self.__options("Downloads").is_displayed() and self.__options("Downloads").is_enabled() == True
        assert self.__options("Downloads").text == "Downloads"

        assert self.__options("Back to JQuery UI").is_displayed() and self.__options(
            "Back to JQuery UI").is_enabled() == True
        assert self.__options("Back to JQuery UI").text == "Back to JQuery UI"

        self.__move_to_element(self.__options("Downloads"), self.__download_expanded_menu_element())
        assert self.__options("PDF").is_displayed() and self.__options("PDF").is_enabled() == True
        assert self.__options("PDF").text == "PDF"

        assert self.__options("CSV").is_displayed() and self.__options("CSV").is_enabled() == True
        assert self.__options("CSV").text == "CSV"

        assert self.__options("Excel").is_displayed() and self.__options("Excel").is_enabled() == True
        assert self.__options("Excel").text == "Excel"

    def click_on_jquery_link(self):
        self.__jQuery_link_element().click()

    def download_all_files(self):
        self.__move_to_element(self.__enabled_option_element(), self.__enable_expanded_menu_element())
        self.__move_to_element(self.__options("Downloads"), self.__download_expanded_menu_element())
        self.__options("PDF").click()
        self.__options("CSV").click()
        self.__options("Excel").click()

    def click_on_menu_option(self, element):
        self.__options(element).click()
        assert self.__headers_page_text() == "JQuery UI"
        assert self.__body_texts()[0].text == "JQuery UI is many things, but one thing specifically that causes " \
                                              "automation challenges is their set of Widgets"
