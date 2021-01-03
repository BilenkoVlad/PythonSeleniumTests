from selenium.webdriver.common.by import By


class file_download_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __files = (By.XPATH, "//div[@class='example']/a")
    __files_names = ['python_18894.png', '1.qisim.jpg', 'uyghurHub.png', 'file for test 1.txt',
                     'Admin Assistant Security Department May 7 2020.docx', 'file_type_flutter_icon_130599.png',
                     'locators.txt', 'javascript_icon_130900.png', '2.qisim.jpg', 'some-file.txt', 'apple.jpg.png',
                     'powerful.jpg', 'april-2560x1440.jpg', 'File.txt', 'not_empty.txt', 'sample.json',
                     'webdriverIO.png', 'ObjectivityTestAutomationCSHarpFramework.txt']

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __files_links(self):
        return self.driver.find_elements(*self.__files)

    def verify_default_content(self):
        assert self.__headers_page_text() == "File Downloader"
        assert len(self.__files_links()) == 18
        for i in range(len(self.__files_links())):
            assert self.__files_links()[i].text in self.__files_names
            assert self.__files_links()[i].tag_name == "a"
            assert self.__files_links()[i].is_displayed() and self.__files_links()[i].is_enabled() == True

    def download_files(self):
        for i in range(len(self.__files_links())):
            self.__files_links()[i].click()
