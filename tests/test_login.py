import unittest
from utils.driver_setup import setup_driver
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = setup_driver()
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login()
        self.assertIn("welcome", self.driver.page_source, "Login failed!")

    def test_invalid_login(self):
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("wrong_password")
        self.login_page.click_login()
        error_message = self.login_page.get_error_message()
        self.assertEqual(error_message, "Invalid credentials", "Error message mismatch!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
