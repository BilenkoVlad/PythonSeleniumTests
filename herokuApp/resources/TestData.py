from random import random

from selenium import webdriver


def browser(browser_name):
    if browser_name == "chrome":
        preferences = {
            "profile.default_content_settings.popups": 0,
            "download.default_directory": r"C:\Users\vladyslav.bilenko\Desktop\PythonSeleniumTests\herokuApp"
                                          r"\resources\downloads\\",
            "directory_upgrade": True,
            "disable-popup-blocking": True,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True
        }
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", preferences)
        driver = webdriver.Chrome(chrome_options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Opera()
    return driver


def email_generator() -> str:
    symbols_for_generator = "abcdefghijklmnopqrstuvxyz0123456789"
    email = ""
    for i in range(10):
        index = int(len(symbols_for_generator) * random())
        email += symbols_for_generator[index]
    return email + "@mailinator.com"


class TestData():
    CHROME_EXECUTABLE_PATH = "resources/drivers/chromedriver.exe"
    BASE_URL = "https://the-internet.herokuapp.com"
