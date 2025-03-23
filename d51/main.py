from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
PROMISED_DOWN = 1000
PROMISED_UP = 1000

service = Service("/usr/bin/chromedriver")


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(5)
        self.driver.find_element(By.CLASS_NAME, value="accept-btn-only").click()

        self.driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[1]/a/span[4]',
        ).click()
        sleep(60)
        self.down = self.driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span',
        ).text
        self.up = self.driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span',
        ).text

        print(f"Download = {self.down} Mbps")
        print(f"Upload = {self.up} Mbps")
        sleep(2)
        twitter_bot.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.maximize_window()
        self.driver.get("https://x.com/i/flow/login")
        sleep(5)
        email = self.driver.find_element(By.NAME, value="text")
        email.send_keys(MY_EMAIL)
        sleep(2)
        email.send_keys(Keys.ENTER)
        sleep(2)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(MY_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)
        self.driver.get("https://x.com/compose/post")
        sleep(5)
        tweet = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span',
        )
        tweet.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down} Mbps Down/{self.up} Mbps Up when I pay for {PROMISED_DOWN} Mbps Down/{PROMISED_UP} Mbps Up?\n\nday51 of #100DaysOfPython\n\n***This is a bot generated X."
        )
        sleep(5)
        self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]',
        ).click()
        sleep(5)
        self.driver.quit()


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
