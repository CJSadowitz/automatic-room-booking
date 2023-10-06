from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Event_Names import a, eventNames
import time

# Make an object of class webdriver.Chrome
driver = webdriver.Chrome()
# Load the desired website
driver.get('https://xxxx.com')

# Find and input user ID
userID = driver.find_element(By.ID, 'userID_input')
userID.send_keys('user-name')  # Missing code for getting specific user ID from list of users

# Find and input user password
userPassword = driver.find_element(By.ID, 'password_input')
userPassword.send_keys('user-password')  # Missing code for getting specific password from list

# Click Sign in button
signIn = driver.find_element(By.ID, 'pc_btnLogin')  # Find a way to ensure successful login
signIn.click()

# Click the 'Book Now' button
bookNow = driver.find_element(By.XPATH, '//*[@id="templates-grid"]/div/div/div[2]/button[1]')
bookNow.click()

specificRoom = driver.find_element(By.XPATH, '//*[@id="location-filter-container"]/div[2]/button')
specificRoom.click()

favoriteRoom_locator = driver.find_element(By.ID, 'favorites-only-chk')
favoriteRoom = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(favoriteRoom_locator))
time.sleep(5)
favoriteRoom.click()
time.sleep(10)

room = driver.find_element(By.CSS_SELECTOR, 'i.book-action-icon.book-add-to-cart.fa.fa-plus-circle')
room.click()

popRoom_locator = driver.find_element(By.ID, 'setup--add-modal-save')
popRoom = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(popRoom_locator))
popRoom.click()
alert = WebDriverWait(driver, 10).until(ec.alert_is_present())
alert.accept()

add_room_locator = (By.ID, 'next-step-btn')
driver.execute_script("window.scrollTo(0, arguments[0].offsetTop);", add_room_locator)
add_room = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(add_room_locator))
add_room.click()

# Find and click Event name
eventName = driver.find_element(By.ID, 'event-name')
eventName.send_keys(eventNames[a])

# Find and click Phone number
phone = driver.find_element(By.ID, '1stContactPhone1')
phone.send_keys('xxx-xxx-xxxx')

# Find and click Create Reservation
reservation = driver.find_element(By.XPATH, '//*[@id="details"]/div[3]/div/span[2]/button')  # find actual ID
reservation.click()
time.sleep(30)

driver.quit()
