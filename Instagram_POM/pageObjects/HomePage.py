from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    Profile = (By.XPATH, "//a[text()='darshan.patel_7696']")
    messages = (By.XPATH, '//span[text()="Messages"]')
    search = (By.XPATH, "//span[text()='Search']")

    def visitProfile(self):
        return self.driver.find_element(*HomePage.Profile)

    def visitmessages(self):
        return self.driver.find_element(*HomePage.messages)

    def visitSearch(self):
        return self.driver.find_element(*HomePage.search)

