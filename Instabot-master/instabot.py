
from instapy import InstaPy

# Bot Login
bot = InstaPy(username="the.pupcompanion", password="9754301892")
bot.login()

# Sending Likes To Posts
hastags = ["dog", "puppy"] #You Could Change/Add Hashtags According To Your Niche/Category 
bot.like_by_tags(hastags, amount=10)

# Following The Posts That Bot Likes
bot.set_do_follow(True, percentage=100)

# Commenting On Posts
bot.set_do_comment(True, percentage=100)
comments = ["Awesome Post", "Great Content, Do Check Page"]
bot.set_comment(comments)

bot.end()
