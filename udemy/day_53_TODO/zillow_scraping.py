import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
ZILLOW_URL = ("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%"
              "22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-"
              "122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22is"
              "MapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%"
              "22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%"
              "2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%"
              "22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%"
              "22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%"
              "22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D")
"""

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/"

class ZillowScraping:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)

        self.links = []
        self.prices = []
        self.addresses = []
        self.driver = driver

    def initialize_lists(self):
        self.driver.get(ZILLOW_URL)
        time.sleep(20)
        articles = self.driver.find_elements((By.TAG_NAME, "article"))

        anchor_tags = self.driver.find_elements(By.CLASS_NAME, 'property-card-link')
        for a in anchor_tags:
            url = a.get_attribute("href")
            self.links.append(url)

        span_prices = self.driver.find_elements(By.CSS_SELECTOR, 'span[data-test="property-card-price"]')
        print(span_prices)

todelete = ZillowScraping()
todelete.initialize_lists()
