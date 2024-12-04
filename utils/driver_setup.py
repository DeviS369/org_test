import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os
load_dotenv()
def setup_driver():
    """Sets up and returns a WebDriver instance."""
    url = os.environ.get('app_url')
    
    # Set up ChromeDriver service
    service = Service(r"C:\orange_hrm\drivers\chromedriver\chromedriver.exe")
    
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service)
    
    # Configure WebDriver
    driver.maximize_window()
    driver.get(url) # Load the application URL
    
    return driver

