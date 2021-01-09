from selenium.webdriver.common.by import By


class frames_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __links = (By.XPATH, "//div[@class='example']/ul/li/a")
    __links_names = ["Nested Frames", "iFrame"]

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __links_elements(self):
        return self.driver.find_elements(*self.__links)

    def verify_default_content(self):
        assert self.__headers_page_text() == "Frames"
        for i in range(len(self.__links_elements())):
            assert self.__links_elements()[i].text == self.__links_names[i]
            assert self.__links_elements()[i].tag_name == "a"

    def click_nested_frames_link(self):
        for i in range(len(self.__links_elements())):
            if self.__links_elements()[i] == "Nested Frames":
                self.__links_elements()[i].click()
