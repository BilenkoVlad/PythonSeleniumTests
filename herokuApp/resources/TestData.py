from selenium import webdriver


def browser(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Opera()
    return driver


class TestData():
    CHROME_EXECUTABLE_PATH = "resources/drivers/chromedriver.exe"
    BASE_URL = "https://the-internet.herokuapp.com"
