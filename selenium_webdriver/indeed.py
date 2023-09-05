from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Indeed website
driver.get("https://in.indeed.com")

# Click the "Sign in" button using By.LINK_TEXT
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# Wait for the login options to load (you can increase or decrease the time if needed)
driver.implicitly_wait(10)

# Click the "Sign in with Google" button
google_sign_in_button = driver.find_element(By.ID, 'login-google-button')
google_sign_in_button.click()

# Switch to the new tab or window that opened for Google login
driver.switch_to.window(driver.window_handles[-1])

# Wait for the email input field to become clickable
email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'identifierId')))

# Use send_keys to enter the email
email_field.send_keys('ravidossalbert@gmail.com')  # Replace with your actual Gmail address

#Tto fill in the password and complete the login process
passWord = driver.find_element(By.ID, 'identifierNext').click()
# To prevent the browser from closing immediately, use a simple input
input("Press Enter to exit...")

# Close the current tab or window (the Google login)
driver.close()

# Switch back to the original tab or window
driver.switch_to.window(driver.window_handles[0])

# Quit the WebDriver
driver.quit()
