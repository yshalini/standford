from pageObjects.loginpage import LoginPage
from utilities.BaseClass import BaseClass
import time
class TestOne(BaseClass):
    def test_e2e(self):
        loginpage= LoginPage(self.driver)
        time.sleep(5000)
        loginpage.getEmail().send_keys("shaliniy@boston-technology.com")
        loginpage.getPassword().send_keys("@New1288")
        time.sleep(100)
        loginpage.getSignin().click()
