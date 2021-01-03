from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class entry_ad_page:
    __modal_window = (By.XPATH, "//div[@class='modal']")
    __modal_window_title = (By.XPATH, "//div[@class='modal-title']/h3")
    __modal_window_text = (By.XPATH, "//div[@class='modal-body']/p")
    __modal_window_close = (By.XPATH, "//div[@class='modal-footer']/p")
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='example']/p")
    __click_here_link = (By.XPATH, "//a[@id='restart-ad']")
    __text = ["Displays an ad on page load.", "If closed, it will not appear on subsequent page loads.",
              "To re-enable it, click here."]

    def __init__(self, driver):
        self.driver = driver

    def __modal_window_element(self):
        return self.driver.find_element(*self.__modal_window)

    def __modal_window_title_text(self):
        return self.driver.find_element(*self.__modal_window_title).text

    def __modal_window_text_text(self):
        return self.driver.find_element(*self.__modal_window_text).text

    def __modal_window_close_element(self):
        return self.driver.find_element(*self.__modal_window_close)

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_text(self):
        return self.driver.find_elements(*self.__body)

    def __click_here_link_element(self):
        return self.driver.find_element(*self.__click_here_link)

    def __wait_for_modal_window(self):
        try:
            web_driver_wait = WebDriverWait(self.driver, 5)
            web_driver_wait.until(EC.visibility_of_element_located(self.__modal_window))
            return True
        except TimeoutException:
            return False

    def verify_default_content_modal_window(self):
        self.__wait_for_modal_window()
        assert self.__modal_window_element().is_displayed() == True
        assert self.__modal_window_title_text() == "This is a modal window".upper()
        assert self.__modal_window_text_text() == "It's commonly used to encourage a user to take an action " \
                                                  "(e.g., give their e-mail address to sign up for something " \
                                                  "or disable their ad blocker)."
        assert self.__modal_window_close_element().text == "Close"

    def verify_default_content(self):
        assert self.__headers_page_text() == "Entry Ad"
        for i in range(len(self.__body_text())):
            assert self.__body_text()[i].text == self.__text[i]
        assert self.__click_here_link_element().tag_name == "a"
        assert self.__click_here_link_element().is_displayed() and self.__click_here_link_element().is_enabled() == True

    def click_close_button(self):
        self.__modal_window_close_element().click()

    def click_on_here_link(self):
        while not self.__wait_for_modal_window():
            self.__click_here_link_element().click()
        self.verify_default_content_modal_window()

    def refresh_page(self):
        while not self.__wait_for_modal_window():
            self.__click_here_link_element().click()
        self.verify_default_content_modal_window()
