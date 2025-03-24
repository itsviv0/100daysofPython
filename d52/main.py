from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time

CHROME_DRIVER_PATH = "/usr/bin/chromedriver"
SIMILAR_ACCOUNT = "pentastrikex"

load_dotenv(".env")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


class InstaFollowerBot:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME, value="username")
        password = self.driver.find_element(By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mount_0_0_U3"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section/div[2]/ul/li[2]/div/button/span',
        )
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(
            By.XPATH,
            value="/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]",
        )

        for _ in range(10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal
            )
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(
            By.CLASS_NAME, value="_ap3a _aaco _aacw _aad6 _aade"
        )
        for button in all_buttons:
            if button.text == "Follow":
                button.click()
                time.sleep(1)


bot = InstaFollowerBot(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
