from datetime import date
import time
from utils.CreateMovie import CreateMovie, GetDaySuffix
from utils.RedditBot import RedditBot
from utils.upload_video import upload_video

#Create Reddit Data Bot
redditbot = RedditBot()

# Leave if you want to run it 24/7
while True:

    # Gets our new posts pass if image related subs. Default is memes
    posts = redditbot.get_posts("dankmemes")

    # Create folder if it doesn't exist
    redditbot.create_data_folder()

    # Go through posts and find 5 that will work for us.
    for post in posts:
        print(post)
        redditbot.save_image(post)

    # Wanted a date in my titles so added this helper
    DAY = date.today().strftime("%d")
    DAY = str(int(DAY)) + GetDaySuffix(int(DAY))
    dt_string = date.today().strftime("%A %B") + f" {DAY}"

    # Create the movie itself!
    CreateMovie.CreateMP4(redditbot.post_data)

    # Video info for YouTube.
    # This example uses the first post title.
    video_data = {
            "file": "video.mp4",
            "title": f"{redditbot.post_data[0]['title']} - Dankest memes and comments {dt_string}!",
            "description": "#shorts\nGiving you the hottest memes of the day with funny comments!",
            "keywords": "meme,redditmeme,dankestmemes",
            "privacyStatus": "public",
    }

    print(video_data["title"])
    print("Posting Video in 2 minutes...")
    time.sleep(60 * 2)
    upload_video(video_data)

    # Sleep until ready to post another video!
    time.sleep(60 * 60 * 6)
