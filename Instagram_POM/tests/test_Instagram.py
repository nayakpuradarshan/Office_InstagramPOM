import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage

class TestOne(BaseClass):

    def test_e2e(self):

        time.sleep(3)
        # Enter username
        TestUserName = LoginPage(self.driver)
        TestUserName.enterUserName().send_keys("darshan.patel_7696")

        # Enter password
        TestPassword = LoginPage(self.driver)
        TestPassword.enterPassWord().send_keys("DV05@insta")

        # Click on login button
        TestLoginButton = LoginPage(self.driver)
        TestLoginButton.clickLoginButton().click()

        wait = WebDriverWait(self.driver, 10)
        # Click on NOT now button
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_ac8f']/div"))).click()

        # CLick on NOT NOW button again on home page
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_a9-z']/button[2]"))).click()

        # refresh feed
        self.driver.refresh()

        # Starting home page

        # visiting profile
        testprofile = HomePage(self.driver)
        testprofile.visitProfile().click()
        time.sleep(4)

        # checking new messaged if any
        self.driver.back()
        testmessages = HomePage(self.driver)
        testmessages.visitmessages().click()
        time.sleep(4)

        self.driver.back()
        # Click on search button
        testsearchfild = HomePage(self.driver)
        testsearchfild.visitSearch().click()

        # search for virat kohli's account
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search input']"))).send_keys(
            "Viral Kohli")

        # Click on virat kohli's account
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Virat Kohli • 269M followers']"))).click()

        # Check how much followers virat has ?
        followers = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='269M']")))
        print(followers.text)
        assert followers.text == "269M"

        # Check how much follwing virat has ?
        following = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="302"]')))
        print(following.text)
        assert following.text == "302"

        # Click on search button on search
        time.sleep(5)
        self.driver.close()
