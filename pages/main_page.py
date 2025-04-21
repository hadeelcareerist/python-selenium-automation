from pages.base_page import Page





class MainPage(Page): #opening target main page
    def open_main_page(self):
        self.open_url('http://www.target.com/')

#header search for something
