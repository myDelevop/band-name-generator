from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# click on an anchor tag
# num_articles_elem = driver.find_element(By.CSS_SELECTOR, 'div#articlecount a[title="Special:Statistics"]')
# num_articles_elem.click()

# easily using By.LINK_TEXT and search for the string
view_source = driver.find_element(By.LINK_TEXT, "View source")
view_source.click()

# Search Python in the search bar
search_bar = driver.find_element(By.CSS_SELECTOR, value="input#searchInput")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
#
# search_button = driver.find_element(By.CSS_SELECTOR, value="form#searchform button")
# search_button.click()


# LAB Report signup
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, "fName")
last_name_input = driver.find_element(By.NAME, "lName")
email_input = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CSS_SELECTOR, "form button")

first_name_input.send_keys("Angelo")
last_name_input.send_keys("Colonio")
email_input.send_keys("angelo.colonio@libero.it")
button.click()
