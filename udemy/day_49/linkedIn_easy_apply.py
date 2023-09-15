import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL")
LINKEDIN_PSW = os.environ.get("LINKEDIN_PSW")


def abort_application():
    # Click Close Button
    x_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    x_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[0]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search?keywords=Sales&location=Bari&geoId="
           "&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

username_input = driver.find_element(By.CSS_SELECTOR, "input#username")
psw_input = driver.find_element(By.CSS_SELECTOR, "input#password")

username_input.send_keys(LINKEDIN_EMAIL)
psw_input.send_keys(LINKEDIN_PSW)
psw_input.send_keys(Keys.ENTER)

input("Press Enter when you have solved the Captcha")

time.sleep(5)
all_jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for job in all_jobs:
    submitted = False
    print("Opening Listing")
    job.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys("123456")

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.text.strip() == "Next":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            submitted = True
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)

        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
