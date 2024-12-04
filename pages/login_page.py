from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH,'''//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button''')
        self.error_message = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.error_message)
        ).text
