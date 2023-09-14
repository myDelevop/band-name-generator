from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

upcoming_events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

events = {}
index = 0
for upcoming_event in upcoming_events:
    events[index] = {
        "time": upcoming_event.text.split("\n")[0],
        "name": upcoming_event.text.split("\n")[1]
    }
    index += 1

print(events)

# driver.quit()
