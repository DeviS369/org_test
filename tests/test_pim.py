import unittest
from utils.driver_setup import setup_driver
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

class TestPIM(unittest.TestCase):
    def setUp(self):
        self.driver = setup_driver()
        self.login_page = LoginPage(self.driver)
        self.pim_page = PIMPage(self.driver)

        # Login first
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login()

    def test_add_employee(self):
        self.pim_page.navigate_to_pim()
        self.pim_page.add_employee("John", "Doe")
        self.assertIn("John", self.driver.page_source, "Employee not added!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
