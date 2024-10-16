import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://127.0.0.1:5000')

    def test_button_exists(self):
        button = self.driver.find_element(By.ID, 'test-button')
        self.assertIsNotNone(button)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
