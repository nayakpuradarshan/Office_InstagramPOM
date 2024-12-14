from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    userName = (By.NAME, "username")
    passWord = (By.NAME, "password")
    loginButton = (By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1'][1]")

    def enterUserName(self):
        return self.driver.find_element(*LoginPage.userName)

    def enterPassWord(self):
        return self.driver.find_element(*LoginPage.passWord)

    def clickLoginButton(self):
        return self.driver.find_element(*LoginPage.loginButton)



