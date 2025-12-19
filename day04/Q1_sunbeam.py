# import required packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# start the selenium browser session
driver = webdriver.Chrome()

# load Sunbeam internship page
driver.get("https://duckduckgo.com/")
print("Page Title:", driver.title)

# define wait strategy
driver.implicitly_wait(5)

search_box = driver.find_element(By.ID, "searchbox_input")
search_box.send_keys("Sunbeam pune")
search_box.send_keys(Keys.RETURN)

link = driver.find_element(By.ID, "r1-0")
link.click()

Inter = driver.find_element(By.PARTIAL_LINK_TEXT, "INTERN")
Inter.click()

# ---------------- SCROLL FIX ADDED HERE ----------------
time.sleep(3)  # wait for page to load
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# ------------------------------------------------------

time.sleep(5)

# stop the session
driver.quit()
