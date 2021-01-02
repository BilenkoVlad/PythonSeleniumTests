from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class context_menu_page:
    __header_page = (By.XPATH, "//div[@class='example']/h3")
    __body_text = (By.XPATH, "//div[@class='example']/p")
    __context_box = (By.CSS_SELECTOR, "#hot-spot")

    def __init__(self, driver):
        self.driver = driver

    def __header_page_text(self, option) -> str:
        return self.driver.find_element(*self.__header_page).text if option == "text" \
            else self.driver.find_element(*self.__header_page)

    def __body_text_list(self) -> list:
        return self.driver.find_elements(*self.__body_text)

    def __context_menu_box(self):
        return self.driver.find_element(*self.__context_box)

    def verify_default_content(self):
        assert self.__header_page_text("text") == "Context Menu"
        assert self.__body_text_list()[0].text == \
               "Context menu items are custom additions that appear in the right-click menu."
        assert self.__body_text_list()[1].text == \
               "Right-click in the box below to see one called 'the-internet'. " \
               "When you click it, it will trigger a JavaScript alert."
        assert self.__context_menu_box().is_displayed() == True

    def __alert_is_present(self) -> bool:
        try:
            self.driver.switch_to_alert()
            return True
        except NoAlertPresentException:
            return False

    def left_click_on_box(self):
        self.__context_menu_box().click()
        assert self.__alert_is_present() == False

    def right_click_out_box(self):
        actions = ActionChains(self.driver)
        actions.context_click(self.__header_page_text("element")).perform()
        assert self.__alert_is_present() == False

    def right_click_on_box(self):
        actions = ActionChains(self.driver)
        actions.context_click(self.__context_menu_box()).perform()
        assert self.__alert_is_present() == True
        assert self.driver.switch_to_alert().text == "You selected a context menu"
        self.driver.switch_to_alert().accept()
        assert self.__alert_is_present() == False
