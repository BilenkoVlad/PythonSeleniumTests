from selenium.webdriver.common.by import By


class basic_auth_page:
    __page_name_text = (By.XPATH, "//div[@class='example']/h3")
    __page_body_text = (By.XPATH, "//div[@class='example']/p")
    __url_with_basic_auth = "the-internet.herokuapp.com/basic_auth"

    def __init__(self, driver):
        self.driver = driver

    def verify_page_text(self):
        page_name_text: str = self.driver.find_element(*self.__page_name_text).text
        page_body_text: str = self.driver.find_element(*self.__page_body_text).text
        assert page_name_text == "Basic Auth"
        assert page_body_text == "Congratulations! You must have the proper credentials."

    def basic_auth_with_credentials(self, user_name, user_password):
        self.driver.get(f"https://{user_name}:{user_password}@{self.__url_with_basic_auth}")
