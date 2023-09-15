import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        self.driver = driver

    def login(self, username, psw):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        decline_btn = self.driver.find_element(By.CSS_SELECTOR, value="button._a9--._a9_1")
        decline_btn.click()
        time.sleep(4)
        email_field = self.driver.find_element(By.CSS_SELECTOR, value='input[name = "username"]')
        email_field.send_keys(username)
        psw_field = self.driver.find_element(By.CSS_SELECTOR, value='input[name = "password"]')
        psw_field.send_keys(psw)
        psw_field.send_keys(Keys.ENTER)

    def find_followers(self, target_account):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{target_account}")
        time.sleep(5)
        #followers_link = self.driver.find_element(By.XPATH, value="//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        followers_link = self.driver.find_element(
            By.CSS_SELECTOR,
            value="a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx"
                  ".xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg"
                  ".xggy1nq.x1a2a7pz._alvs._a6hd")
        followers_link.click()

        time.sleep(2)
        # modal = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]')
        modal = self.driver.find_element(By.CSS_SELECTOR, value="div._aano")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        time.sleep(10)
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "div._aano button")
        for button in buttons:
            try:
                time.sleep(10)
                button.click()
            except ElementClickInterceptedException:
                time.sleep(10)
                cancel_btn = self.driver.find_element(By.CSS_SELECTOR, value="button._a9--._a9_1")
                cancel_btn.click()


