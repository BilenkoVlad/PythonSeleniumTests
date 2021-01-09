from selenium.webdriver.common.by import By


class sortable_data_tables_page:
    __headers_page = (By.XPATH, "//div[@class='example']/h3")
    __body = (By.XPATH, "//div[@class='example']/p")
    __example_title = (By.XPATH, "//div[@class='example']/h4")
    __table_one = (By.XPATH, "//table[@id='table1']")
    __table_one_headers = (By.XPATH, "//table[@id='table1']//th")
    __table_one_records = (By.XPATH, "//table[@id='table1']//td")
    __table_two = (By.XPATH, "//table[@id='table2']")
    __table_two_headers = (By.XPATH, "//table[@id='table2']//th")
    __table_two_records = (By.XPATH, "//table[@id='table2']//td")

    def __init__(self, driver):
        self.driver = driver

    def __headers_page_text(self):
        return self.driver.find_element(*self.__headers_page).text

    def __body_texts(self):
        return self.driver.find_elements(*self.__body)

    def __example_title_elements(self):
        return self.driver.find_elements(*self.__example_title)

    def __table_one_element(self):
        return self.driver.find_element(*self.__table_one)

    def __table_one_headers_elements(self):
        return self.driver.find_elements(*self.__table_one_headers)

    def __table_one_records_elements(self):
        return self.driver.find_elements(*self.__table_one_records)

    def __table_two_element(self):
        return self.driver.find_element(*self.__table_two)

    def __table_two_headers_elements(self):
        return self.driver.find_elements(*self.__table_two_headers)

    def __table_two_records_elements(self):
        return self.driver.find_elements(*self.__table_two_records)

    def verify_default_content(self):
        assert self.__headers_page_text() == "Data Tables"
        assert self.__body_texts()[0].text == "Often times when you see a table it contains data which is sortable" \
                                              " -- sometimes with actions that can be taken within each row " \
                                              "(e.g. edit, delete). And it can be challenging to automate inter" \
                                              "action with sets of data in a table depending on how it is constructed."
        for i in range(len(self.__example_title_elements())):
            assert self.__example_title_elements()[i].text == f"Example {i + 1}"
        assert self.__body_texts()[1].text == "No Class or ID attributes to signify groupings of rows and columns"
        assert self.__body_texts()[2].text == "Class and ID attributes to signify groupings of rows and columns"
        assert self.__table_one_element().is_displayed() and self.__table_two_element().is_displayed() == True
        assert len(self.__table_one_records_elements()) == len(self.__table_two_records_elements())
        for i in range(len(self.__table_one_headers_elements())):
            assert self.__table_one_headers_elements()[i].text == self.__table_two_headers_elements()[i].text
        for i in range(len(self.__table_one_records_elements())):
            assert self.__table_one_records_elements()[i].text == self.__table_two_records_elements()[i].text

    def sort_table_by_each_header_asc(self):
        for i in range(len(self.__table_one_headers_elements())):
            self.__table_one_headers_elements()[i].click()
            self.__table_two_headers_elements()[i].click()
            for j in range(len(self.__table_one_records_elements())):
                assert self.__table_one_records_elements()[j].text == self.__table_two_records_elements()[j].text

    def sort_table_by_each_header_desc(self):
        for i in range(len(self.__table_one_headers_elements())):
            self.__table_one_headers_elements()[i].click()
            self.__table_two_headers_elements()[i].click()
            for j in range(len(self.__table_one_records_elements())):
                assert self.__table_one_records_elements()[j].text == self.__table_two_records_elements()[j].text
