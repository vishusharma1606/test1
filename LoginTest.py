import unittest
import HtmlTestRunner
import time
from selenium import webdriver


import os

from testbed.loginpage import LoginPage
import sys
sys.path.append("C:/Users/vishv/Desktop/1.2/testbed")


class LoginTest(unittest.TestCase):
    baseURL = "https://10.4.5.216"
    USERNAME = "superadmin"
    PASSWORD = "Admin@123"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\vishv\\Desktop\\1.2\\Drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.enter_username(self.USERNAME)
        lp.enter_password(self.PASSWORD)
        lp.click_login()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vishv\\Desktop\\1.2\\reports'))
