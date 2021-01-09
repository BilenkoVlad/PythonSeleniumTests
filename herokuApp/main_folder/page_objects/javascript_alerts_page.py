from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class javascript_alerts_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='example']/p")
    __result = (By.XPATH, "//div[@class='example']/h4")
    __result_message = (By.XPATH, "//p[@id='result']")
    __js_buttons = (By.XPATH, "//button")
    __js_alert = (By.XPATH, "//button[@onclick='jsAlert()']")
    __js_confirm = (By.XPATH, "//button[@onclick='jsConfirm()']")
    __js_prompt = (By.XPATH, "//button[@onclick='jsPrompt()']")
    __js_names = ["Click for JS Alert", "Click for JS Confirm", "Click for JS Prompt"]

    def __init__(self, driver):
        self.driver = driver

    def __js_buttons_elements(self):
        return self.driver.find_elements(*self.__js_buttons)

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_text(self):
        return self.driver.find_element(*self.__body).text

    def __result_text(self):
        return self.driver.find_element(*self.__result).text

    def __result_message_text(self):
        return self.driver.find_element(*self.__result_message).text

    def __js_alert_element(self):
        return self.driver.find_element(*self.__js_alert)

    def __js_confirm_element(self):
        return self.driver.find_element(*self.__js_confirm)

    def __js_prompt_element(self):
        return self.driver.find_element(*self.__js_prompt)

    def __wait_for_alert(self):
        web_driver_wait = WebDriverWait(self.driver, 5)
        web_driver_wait.until(EC.alert_is_present())

    def __get_alert_text(self):
        return self.driver.switch_to_alert().text

    def verify_default_content(self):
        assert self.__headers_page_text() == "JavaScript Alerts"
        assert self.__body_text() == "Here are some examples of different JavaScript alerts which " \
                                     "can be troublesome for automation"
        for i in range(len(self.__js_buttons_elements())):
            assert self.__js_buttons_elements()[i].is_displayed() and self.__js_buttons_elements()[i].is_enabled() \
                   == True
            assert self.__js_buttons_elements()[i].text == self.__js_names[i]

        assert self.__result_text() == "Result:"
        assert self.__result_message_text() == ""

    def click_on_js_alert(self):
        self.__js_alert_element().click()
        self.__wait_for_alert()
        assert self.__get_alert_text() == "I am a JS Alert"
        self.driver.switch_to_alert().accept()
        assert self.__result_message_text() == "You successfuly clicked an alert"

    def click_on_js_confirm(self, action):
        self.__js_confirm_element().click()
        self.__wait_for_alert()
        assert self.__get_alert_text() == "I am a JS Confirm"
        if action == "OK":
            self.driver.switch_to_alert().accept()
            assert self.__result_message_text() == "You clicked: Ok"
        else:
            self.driver.switch_to_alert().dismiss()
            assert self.__result_message_text() == "You clicked: Cancel"

    def click_on_js_prompt_with_text(self, action, text):
        self.__js_prompt_element().click()
        self.__wait_for_alert()
        assert self.__get_alert_text() == "I am a JS prompt"
        if action == "OK":
            self.driver.switch_to_alert().send_keys(text)
            self.driver.switch_to_alert().accept()
            assert self.__result_message_text() == f"You entered: {text}"
        else:
            self.driver.switch_to_alert().send_keys(text)
            self.driver.switch_to_alert().dismiss()
            assert self.__result_message_text() == "You entered: null"

    def click_on_js_prompt_without_text(self, action):
        self.__js_prompt_element().click()
        self.__wait_for_alert()
        assert self.__get_alert_text() == "I am a JS prompt"
        if action == "OK":
            self.driver.switch_to_alert().accept()
            assert self.__result_message_text() == "You entered:"
        else:
            self.driver.switch_to_alert().dismiss()
            assert self.__result_message_text() == "You entered: null"
