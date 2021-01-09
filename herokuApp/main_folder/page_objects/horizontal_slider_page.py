from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class horizontal_slider_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='example']/h4")
    __slider = (By.XPATH, "//input")
    __range_number = (By.XPATH, "//span[@id='range']")
    __range_values_keyboard = ["0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5"]
    __range_values_up_mouse = ["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "3.5", "4", "4.5", "5"]
    __rangeValuesDown = ["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5"]

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_text(self):
        return self.driver.find_element(*self.__body).text

    def __slider_element(self):
        return self.driver.find_element(*self.__slider)

    def __range_number_text(self):
        return self.driver.find_element(*self.__range_number).text

    def verify_default_content(self):
        assert self.__headers_page_text() == "Horizontal Slider"
        assert self.__body_text() == "Set the focus on the slider (by clicking on it) and use the arrow keys to " \
                                     "move it right and left. Or click and drag the slider with your mouse. " \
                                     "It will indicate the value of the slider to the right."
        assert self.__slider_element().is_displayed() and self.__slider_element().is_enabled() == True
        assert self.__range_number_text() == "0"

    def move_slider_up_by_keyboard(self):
        actions = ActionChains(self.driver)
        for i in range(0, 50, 5):
            actions.move_to_element_with_offset(self.__slider_element(), -25, 0)
            self.__slider_element().send_keys(Keys.ARROW_UP)
            assert self.__range_number_text() == self.__range_values_keyboard[int(i / 5)]

    def move_slider_down_by_keyboard(self):
        actions = ActionChains(self.driver)
        for i in range(45, 0, -5):
            actions.move_to_element_with_offset(self.__slider_element(), -25, 0)
            self.__slider_element().send_keys(Keys.ARROW_DOWN)
            assert self.__range_number_text() == self.__rangeValuesDown[int(i / 5)]
