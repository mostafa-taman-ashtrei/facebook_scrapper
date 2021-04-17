from dotenv import load_dotenv
from selenium import webdriver

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
        pass

    def download(self):
        pass


scraper = FBScraper()
