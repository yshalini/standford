import time

import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(executable_path ="C:/Users\Shalini\Downloads\chromedriver_win32 (2)//chromedriver.exe")
driver.maximize_window()
print("open browser")
time.sleep(5)
driver.get("https://studies-som-mhc3-qa.stanford.edu/studybuilder/login.do")
