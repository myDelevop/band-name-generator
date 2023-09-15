import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_driver = driver
        self.down = None
        self.up = None

    def get_internet_speed(self):
        driver.get("https://www.speedtest.net")
        go_btn = driver.find_element(By.CSS_SELECTOR, "div.start-button a[role='button']")
        go_btn.click()
        time.sleep(60)
        values = driver.find_elements(By.CSS_SELECTOR, ".result-item .result-data-value")

        self.down = round(float(values[0].text), 2)
        self.up = round(float(values[1].text), 2)

    def tweet_at_provider(self, promise_down, promise_up, twitter_email, twitter_psw):
        message = (f"Hey Internet Provider, why is my  Internet speed {self.down}down/{self.up}up"
                   f" when I pay for {promise_down}down/{promise_up}up?")
        driver.get("https://twitter.com/")
        sign_in_btn = driver.find_element(By.CSS_SELECTOR, "a[data-testid='loginButton']")
        driver.execute_script("arguments[0].click();", sign_in_btn)

        time.sleep(3)
        sign_in_input = driver.find_element(By.CSS_SELECTOR, value="input[type='text']")
        sign_in_input.send_keys(twitter_email)

        next_btn = driver.find_element(By.XPATH,
                                       value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/"
                                             "div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        next_btn.click()

        time.sleep(3)
        psw_input = driver.find_element(By.XPATH,
                                        value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/"
                                              "div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label")

        psw_input.send_keys(twitter_psw)

        login_btn = driver.find_element(By.XPATH,
                                        value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]"
                                              "/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
        login_btn.click()

        time.sleep(6)

        whats_happening = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        whats_happening.click()
        whats_happening.send_keys(message)
        whats_happening.send_keys(Keys.CONTROL, Keys.ENTER)
        time.sleep(2)

        x_button = driver.find_element(By.XPATH,
                                       value="//*[@id='layers']/div[3]/div/div/div/div/div/div"
                                             "[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div")
        x_button.click()

