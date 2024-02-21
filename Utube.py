import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Add this import statement
from selenium.common.exceptions import NoSuchElementException

class music():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com")
        time.sleep(5)  # Adding a delay to ensure the page is fully loaded
        try:
            search_input = self.driver.find_element("css selector", "input#search")
            search_input.send_keys(self.query)
            search_input.send_keys(Keys.RETURN)
            time.sleep(5)  # Adding a delay to ensure search results are loaded
            video = self.driver.find_element(By.XPATH, '//a[@id="video-title"]')
            # After finding the video element
            # After finding the video element
            self.driver.execute_script("arguments[0].click();", video)


            print("Video found:", video.text)
        except NoSuchElementException:
            print("Video not found.")


