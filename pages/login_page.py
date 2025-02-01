from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
load_dotenv()
class LoginPage:
    username = os.environ.get('VALID_USERNAME')
    password = os.environ.get('VALID_PASSWORD')
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.execute_script("""return document.evaluate(
        '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input', 
        document, 
        null, 
        XPathResult.FIRST_ORDERED_NODE_TYPE, 
        null
             ).singleNodeValue;
        """)

        self.password_input = driver.execute_script("""
            return document.evaluate(
                '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input', 
                document, 
                null, 
                XPathResult.FIRST_ORDERED_NODE_TYPE, 
                null
            ).singleNodeValue;
        """)
        self.login_button = driver.execute_script("""
        return document.evaluate(
            '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button', 
            document, 
            null, 
            XPathResult.FIRST_ORDERED_NODE_TYPE, 
            null
        ).singleNodeValue;
        """)

        self.error_message = driver.execute_script("""
            return document.evaluate(
                '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p', 
                document, 
                null, 
                XPathResult.FIRST_ORDERED_NODE_TYPE, 
                null
            ).singleNodeValue;
        """)

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located(self.error_message)
        ).text

