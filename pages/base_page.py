class Page:

    def __init__(self, driver):
        self.driver = driver #attribute driver inside the class page

#page = Page("driver")
#print(page.driver)
    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
       return self.driver.find_element(*locator)
    def find_elements(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text,  *locator):
        self.driver.find_element(*locator).send_keys(text)

#until here just blueprint

