from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num_articles_elem = driver.find_element(By.CSS_SELECTOR, 'div#articlecount a[title="Special:Statistics"]')

num_articles = int(num_articles_elem.text.replace(",", "").replace(".", ""))

print(num_articles)

