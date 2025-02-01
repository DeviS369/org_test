from selenium.webdriver.common.by import By

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.ID, "menu_pim_viewPimModule")
        self.add_employee_button = (By.ID, "btnAdd")
        #add_employee_button = driver.execute_script("return document.getElementById('btnAdd');")
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.save_button = (By.ID, "btnSave")

    def navigate_to_pim(self):
        self.driver.find_element(*self.pim_menu).click()

    def add_employee(self, first_name, last_name):
        self.driver.find_element(*self.add_employee_button).click()
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()
