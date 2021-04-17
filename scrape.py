from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os


class FBScraper:
    def __init__(self):
        load_dotenv()  # allows us to get env variables
        driver_path = 'D:\chromedriver.exe'  # path to chrome driver

        # disable notifications and alerts
        chrome_options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values.notifications': 2}
        chrome_options.add_experimental_option('prefs', prefs)

        # Initializing driver and opening facebook
        driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
        driver.get('https://facebook.com')
        self.driver = driver

    def login(self):
        # Inputs and button
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=\'email\']')))

        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=\'pass\']')))

        submit_button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[type=\'submit\']')))

        # enter the login info and login
        username_input.clear()
        username_input.send_keys(os.getenv('fusername'))

        password_input.clear()
        password_input.send_keys(os.getenv('password'))

        submit_button.click()

    def download(self):
        pass


scraper = FBScraper()
scraper.login()
