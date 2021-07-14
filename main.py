from selenium import webdriver
from time import sleep

TWITTER_USERNAME = YOUR TWITTER USERNAME
TWITTER_PASSWORD = YOUR TWITTER PASSWORD
CHROME_DRIVER_PATH = YOUR CHROME DRIVER PATH

PROMISED_UP = 5
PROMISED_DOWN = 50


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_driver_path = CHROME_DRIVER_PATH
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.up = ""
        self.down = ""

    def get_internet_speed(self):
        # Get internet upload and download speeds and turn them into integers
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element_by_class_name("js-start-test")
        start_button.click()
        sleep(60)
        download_speed = self.driver.find_element_by_class_name("download-speed")
        upload_speed = self.driver.find_element_by_class_name("upload-speed")
        self.down = int(download_speed.text)
        self.up = int(upload_speed.text)
        return self.down
        return self.up

    def tweet_at_provider(self):
        # login to twitter
        self.driver.get("https://twitter.com/")
        sleep(3)
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        login_button.click()
        sleep(4)
        username_input = self.driver.find_element_by_name("session[username_or_email]")
        username_input.send_keys(TWITTER_USERNAME)
        pass_input = self.driver.find_element_by_name("session[password]")
        pass_input.send_keys(TWITTER_PASSWORD)
        twitter_login_btn = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        twitter_login_btn.click()
        sleep(3)

        # Compose tweet
        compose_tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        compose_tweet.click()
        draft_editor = self.driver.find_element_by_class_name("public-DraftEditor-content")
        draft_editor.send_keys(f"Hey @GetSpectrum why is my internet speed "
                               f"{self.down}down/{self.up}up when I pay for 200mps?")


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()

if twitter_bot.up < PROMISED_UP and twitter_bot.down < PROMISED_DOWN:
    twitter_bot.tweet_at_provider()


