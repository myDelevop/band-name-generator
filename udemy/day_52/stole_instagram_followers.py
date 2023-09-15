from instagram_follower import InstaFollower
import os

TARGET_ACCOUNT = "chefsteps"
INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")


insta_follower = InstaFollower()

insta_follower.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
insta_follower.find_followers(TARGET_ACCOUNT)

insta_follower.follow()
