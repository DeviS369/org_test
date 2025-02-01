import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
load_dotenv()
def setup_driver():
    try:
        app_url = os.environ.get("APP_URL")
        # Initialize ChromeDriver
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(app_url)
        return driver
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        raise
setup_driver()
