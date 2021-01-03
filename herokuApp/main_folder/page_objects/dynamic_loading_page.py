from selenium.webdriver.common.by import By


class dynamic_loading_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='example']/p")
    __body_links = (By.XPATH, "//div[@class='example']/a")
    __text1 = "It's common to see an action get triggered that returns a result dynamically. " \
              "It does not rely on the page to reload or finish loading. The page automatically gets updated " \
              "(e.g. hiding elements, showing elements, updating copy, etc) through the use of JavaScript."
    __text2 = "There are two examples. One in which an element already exists on the page but it" \
              " is not displayed. And anonther where the element is not on the page and gets added in."
    __links_text = ["Example 1: Element on page that is hidden", "Example 2: Element rendered after the fact"]
    __body_texts = [__text1, __text2]

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_text_elements(self):
        return self.driver.find_elements(*self.__body)

    def __body_links_elements(self):
        return self.driver.find_elements(*self.__body_links)

    def verify_default_content(self):
        assert self.__headers_page_text() == "Dynamically Loaded Page Elements"
        for i in range(len(self.__body_links_elements())):
            assert self.__body_links_elements()[i].text == self.__links_text[i]
        for j in range(len(self.__body_text_elements())):
            assert self.__body_text_elements()[j].text == self.__body_texts[j]

    def click_on_first_link(self):
        self.__body_links_elements()[0].click()

    def click_on_second_link(self):
        self.__body_links_elements()[1].click()
