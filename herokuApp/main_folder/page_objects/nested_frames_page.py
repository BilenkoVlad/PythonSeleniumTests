from selenium.webdriver.common.by import By


class nested_frames_page:
    __middle_frameset = (By.XPATH, "//frame[@name='frame-top']")
    __left_frame = (By.XPATH, "//frame[@name='frame-left']")
    __middle_frame = (By.XPATH, "//frame[@name='frame-middle']")
    __right_frame = (By.XPATH, "//frame[@src='/frame_right']")
    __bottom_frame = (By.XPATH, "//frame[@name='frame-bottom']")
    __middle_text = (By.XPATH, "//div[@id='content']")
    __text = (By.XPATH, "//body")

    def __init__(self, driver):
        self.driver = driver

    def __left_frame_action(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.__middle_frameset))
        self.driver.switch_to.frame(self.driver.find_element(*self.__left_frame))
        assert self.driver.find_element(*self.__text).text.strip() == "LEFT"
        self.driver.switch_to_default_content()

    def __middle_frame_action(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.__middle_frameset))
        self.driver.switch_to.frame(self.driver.find_element(*self.__middle_frame))
        assert self.driver.find_element(*self.__middle_text).text.strip() == "MIDDLE"
        self.driver.switch_to_default_content()

    def __right_frame_action(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.__middle_frameset))
        self.driver.switch_to.frame(self.driver.find_element(*self.__right_frame))
        assert self.driver.find_element(*self.__text).text.strip() == "RIGHT"
        self.driver.switch_to_default_content()

    def __bottom_frame_action(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.__bottom_frame))
        print(self.driver.find_element(*self.__text).text.strip())
        assert self.driver.find_element(*self.__text).text.strip() == "BOTTOM"
        # self.driver.switch_to_default_content()

    def check_names(self):
        # self.__left_frame_action()
        # self.__middle_frame_action()
        # self.__right_frame_action()
        self.__bottom_frame_action()
