import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, NoSuchElementException

class inflow():
    def __init__(self):
        try:
            # Set the path to the Chrome webdriver executable
            chromedriver_path = r'C:\Users\2003u\.cache\selenium\chromedriver\win64\121.0.6167.184\chromedriver.exe'

            # Set the PATH environment variable to include the directory containing the Chrome webdriver executable
            os.environ['PATH'] += os.pathsep + os.path.dirname(chromedriver_path)

            # Initialize the Chrome webdriver without specifying the executable path
            self.driver = webdriver.Chrome()
        except WebDriverException as e:
            print("WebDriver initialization failed:", e)

    def get_info(self, query):
        try:
            self.query = query
            self.driver.get(url="https://www.wikipedia.org")
            time.sleep(2)  # Wait for the page to load completely
            search_input = self.driver.find_element("css selector", "#searchInput")
            search_input.send_keys(self.query)
            search_input.send_keys(Keys.RETURN)
        except NoSuchElementException as e:
            print("Element not found:", e)






