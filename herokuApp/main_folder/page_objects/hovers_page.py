from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class hovers_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='example']/p")
    __avatars = (By.XPATH, "//div[@class='figure']")
    __avatars_names = (By.XPATH, "//div[@class='figcaption']/h5")
    __avatars_links = (By.XPATH, "//div[@class='figcaption']/a")
    __avatar_names_expected = ["name: user1", "name: user2", "name: user3"]

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_text(self):
        return self.driver.find_element(*self.__body).text

    def __avatars_elements(self):
        return self.driver.find_elements(*self.__avatars)

    def __avatars_names_elements(self):
        return self.driver.find_elements(*self.__avatars_names)

    def __avatars_links_elements(self):
        return self.driver.find_elements(*self.__avatars_links)

    def verify_default_content(self):
        assert self.__headers_page_text() == "Hovers"
        assert self.__body_text() == "Hover over the image for additional information"
        for i in range(len(self.__avatars_elements())):
            assert self.__avatars_elements()[i].is_displayed() == True
            assert self.__avatars_names_elements()[i].is_displayed() == False
            assert self.__avatars_links_elements()[i].is_displayed() == False

    def hover_each_avatar(self):
        actions = ActionChains(self.driver)
        for i in range(len(self.__avatars_elements())):
            actions.move_to_element(self.__avatars_elements()[i]).release().perform()
            assert self.__avatars_names_elements()[i].is_displayed() \
                   and self.__avatars_links_elements()[i].is_displayed() == True
            assert self.__avatars_names_elements()[i].text == self.__avatar_names_expected[i]
            assert self.__avatars_links_elements()[i].text == "View profile"
