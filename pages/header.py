from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search(self): #search will use input_text because you are searching for tea
        print('Searching for {text}')
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
