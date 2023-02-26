from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from login.keyvalues import*
from utilities.utilities import*
from login.login import LoginScripts
import unittest
import os

class TC01_LoginToApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ['webdriver.chrome.driver'] = 'Z:\\OPSQC\\Selenium\\chromedriver.exe'

    def setUp(self):
        self.driver = get_local_webdriver()
        self.appid="PHWIL-55"
        self.wait = WebDriverWait(self.driver, 5)
        self.login_script = LoginScripts(self.driver, self.wait,self.appid)

    def test_loginToApp(self):
        self.login_script.sign_in()

    # def tearDown(self):
    #     if self.driver:
    #         self.driver.quit()

if __name__ == '__main__':    
    # oracle.connect()
    unittest.main()
