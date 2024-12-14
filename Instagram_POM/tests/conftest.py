import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):

    options = Options()
    # Specify the path to the ChromeDriver
    service_obj = Service(
        executable_path="D:/Darshan/PERSONAL/Python Automation/chromedriver-win64/chromedriver.exe")
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=service_obj, options=options)
    driver.get("https://www.instagram.com/")
    driver.maximize_window()

    request.cls.driver = driver
    # yield
    # driver.close()


