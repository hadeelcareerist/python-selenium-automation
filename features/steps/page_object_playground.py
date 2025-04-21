# Base => blueprint
# page: click / input text /find element , etc .

class Page:
    def click(self):
        print('clicking...')

    def find_element(self):
        print('searching for element...')

    def verify_text(self, actual_text):
        print(f'verify {actual_text}')
#until here blueprint

class Mainpage(Page):
    def open_main(self):
        print('opening main page')

class LoginPage(Page):
    def login(self):
        print('login')

login_page = LoginPage()
login_page.login()
login_page.click()
login_page.find_element()




