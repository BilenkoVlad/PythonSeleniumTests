from selenium.webdriver.common.by import By
import requests


class status_codes_pages:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='example']/p")
    __codes_link = (By.XPATH, "//div[@class='example']//li/a")
    __codes_statuses = [200, 301, 404, 500]

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_text(self):
        return self.driver.find_element(*self.__body).text

    def __codes_link_elements(self):
        return self.driver.find_elements(*self.__codes_link)

    def verify_default_content(self):
        assert self.__headers_page_text() == "Status Codes"
        assert self.__body_text() == "HTTP status codes are a standard set of numbers used to communicate from a web" \
                                     " server to your browser to indicate the outcome of the request being made " \
                                     "(e.g. Success, Redirection, Client Error, Server Error). For a complete list " \
                                     "of status codes, go here.\n\nSome standard status codes you will run into " \
                                     "include but are not limited to:"
        for i in range(len(self.__codes_link_elements())):
            assert self.__codes_link_elements()[i].text == str(self.__codes_statuses[i])

    def click_on_200_code(self):
        self.__codes_link_elements()[0].click()
        request = requests.get(self.driver.current_url)
        assert request.status_code == self.__codes_statuses[0]

    def click_on_301_code(self):
        self.__codes_link_elements()[1].click()
        request = requests.get(self.driver.current_url)
        assert request.status_code == self.__codes_statuses[1]

    def click_on_404_code(self):
        self.__codes_link_elements()[2].click()
        request = requests.get(self.driver.current_url)
        assert request.status_code == self.__codes_statuses[2]

    def click_on_500_code(self):
        self.__codes_link_elements()[3].click()
        request = requests.get(self.driver.current_url)
        assert request.status_code == self.__codes_statuses[3]
