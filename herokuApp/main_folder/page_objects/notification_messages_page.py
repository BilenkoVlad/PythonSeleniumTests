from selenium.webdriver.common.by import By


class notification_messages_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='example']/p")
    __click_here_link = (By.XPATH, "//div[@class='example']/p/a")
    __notification = (By.XPATH, "//div[@id='flash']")
    __text = ['The', 'message', 'displayed', 'above', 'the', 'heading', 'is', 'a', 'notification', 'message.', 'It',
              'is', 'often', 'used', 'to', 'convey', 'information', 'about', 'an', 'action', 'previously', 'taken',
              'by', 'the', 'user.', 'Some', 'rudimentary', 'examples', 'include', "'Action", "successful',", "'Action",
              'unsuccessful,', 'please', 'try', "again',", 'etc.', 'Click', 'here', 'to', 'load', 'a', 'new',
              'message.']
    __notification_text = ["Action unsuccesful, please try again×", "Action successful×"]

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_text(self):
        return self.driver.find_element(*self.__body).text

    def __click_here_link_element(self):
        return self.driver.find_element(*self.__click_here_link)

    def __notification_element(self):
        return self.driver.find_element(*self.__notification)

    def verify_default_content(self):
        assert self.__headers_page_text() == "Notification Message"
        assert self.__body_text().split() == self.__text
        for i in range(2):
            if self.__notification_element().text.strip() == self.__notification_text[i]:
                assert self.__notification_element().text.strip() == self.__notification_text[i]
                assert self.__notification_element().is_displayed() == True
        assert self.__click_here_link_element().is_displayed() and self.__click_here_link_element().is_enabled() == True
