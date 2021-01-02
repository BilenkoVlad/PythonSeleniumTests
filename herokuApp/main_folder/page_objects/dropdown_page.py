from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class dropdown_page:
    __header_page = (By.XPATH, "//div[@class='example']/h3")
    __dropdown = (By.XPATH, "//select[@id='dropdown']")
    __dropdown_options = (By.XPATH, "//select[@id='dropdown']//option")
    __selected_option = (By.XPATH, "//select[@id='dropdown']//option[@selected]")
    __expected_options = ["Please select an option", "Option 1", "Option 2"]

    def __init__(self, driver):
        self.driver = driver

    def __header_page_text(self):
        return self.driver.find_element(*self.__header_page).text

    def __dropdown_element(self):
        return self.driver.find_element(*self.__dropdown)

    def __selected_dropdown_option(self):
        return self.driver.find_element(*self.__selected_option)

    def __dropdown_options_element(self):
        return self.driver.find_elements(*self.__dropdown_options)

    def verify_default_content(self):
        assert self.__header_page_text() == "Dropdown List"
        assert self.__dropdown_element().is_displayed() & self.__dropdown_element().is_enabled() == True
        assert self.__dropdown_options_element()[0].get_attribute("selected") == "true"
        for i in range(len(self.__dropdown_options_element())):
            assert self.__dropdown_options_element()[i].text == self.__expected_options[i]

    def select_option_from_dropdown(self, value):
        select = Select(self.__dropdown_element())
        select.select_by_visible_text(value)
        assert self.__selected_dropdown_option().text == value
        assert self.__selected_dropdown_option().is_selected() == True
        assert self.__dropdown_options_element()[0].is_enabled() == False
