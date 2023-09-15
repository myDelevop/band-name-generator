import os
from internet_speed_twitter_bot import InternetSpeedTwitterBot

PROMISE_DOWN = 60
PROMISE_UP = 20


# TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_EMAIL = "yanove73662"
TWITTER_PASSWORD = os.environ.get("TWITTER_PSW")


speed_twitter_bot = InternetSpeedTwitterBot()
speed_twitter_bot.get_internet_speed()

print("down: " + str(speed_twitter_bot.down))
print("up: " + str(speed_twitter_bot.up))


if speed_twitter_bot.down < PROMISE_DOWN or speed_twitter_bot.up < PROMISE_UP:
    speed_twitter_bot.tweet_at_provider(PROMISE_DOWN, PROMISE_UP, TWITTER_EMAIL, TWITTER_PASSWORD)
