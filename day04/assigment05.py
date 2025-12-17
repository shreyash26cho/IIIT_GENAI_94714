from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.chrome()
driver.get("https://www.sunbeaminfo.in/")
print("initail page tittle :",driver.title)
driver.implicity_wait(5)