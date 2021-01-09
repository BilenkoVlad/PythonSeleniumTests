from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class key_presses_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='example']/p")
    __input_field = (By.XPATH, "//input[@id='target']")
    __result = (By.XPATH, "//p[@id='result']")

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_text(self):
        return self.driver.find_element(*self.__body).text

    def __input_field_element(self):
        return self.driver.find_element(*self.__input_field)

    def __result_text(self):
        return self.driver.find_element(*self.__result)

    def verify_default_content(self):
        assert self.__headers_page_text() == "Key Presses"
        assert self.__body_text() == "Key presses are often used to interact with a website " \
                                     "(e.g., tab order, enter, escape, etc.). Press a key and see what you inputted."
        assert self.__input_field_element().is_displayed() and self.__input_field_element().is_enabled() == True
        assert self.__result_text().is_displayed() == False
        assert self.__result_text().text == ""

    def press_keys_on_page(self):
        actions = ActionChains(self.driver)

        actions.send_keys(Keys.ARROW_UP).release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: UP"

        actions.send_keys(Keys.ARROW_DOWN).release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: DOWN"

        actions.send_keys(Keys.ARROW_LEFT).release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: LEFT"

        actions.send_keys(Keys.ARROW_RIGHT).release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: RIGHT"

        actions.send_keys(Keys.ENTER).release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: ENTER"

        actions.send_keys(Keys.CONTROL).release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: CONTROL"

        actions.send_keys(Keys.SHIFT).release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: SHIFT"

        actions.send_keys(Keys.TAB).release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: TAB"

        actions.send_keys(Keys.ESCAPE).release().perform()

    def press_chars_on_page(self):
        actions = ActionChains(self.driver)

        actions.send_keys("a").release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: A"

        actions.send_keys("q").release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: Q"

        actions.send_keys("c").release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: C"

        actions.send_keys(",").release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: COMMA"

        actions.send_keys("/").release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: SLASH"

        actions.send_keys("[").release().perform()
        assert self.__result_text().is_displayed() == True
        assert self.__result_text().text == "You entered: OPEN_BRACKET"
