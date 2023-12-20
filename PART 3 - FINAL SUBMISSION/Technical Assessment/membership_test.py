from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage with the membership subscription form
driver.get("https://musicplaylist.com/membership-form")

# Locate the input fields and submit button
membership_type_dropdown = Select(driver.find_element(By.ID, "membership_type"))
duration_input = driver.find_element(By.ID, "duration")
submit_button = driver.find_element(By.ID, "submit_button")

# Select subscription type from dropdown
membership_type_dropdown.select_by_visible_text("Gold Membership")

# Enter duration
duration_input.send_keys("12")

# Click the submit button
submit_button.click()

# Wait for a few seconds to see the result
time.sleep(5)

# Close the browser window
driver.quit()
