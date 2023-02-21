from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    email= (By.ID,"email")
    password=(By.ID,"password")
    signin=(By.ID,"loginBtnId")
    def getEmail(self):
            return self.driver.find_element(*LoginPage.email)
    def getPassword(self):
            return self.driver.find_element(*LoginPage.password)
    def getSignin(self):
            return self.driver.find_element(*LoginPage.signin)
