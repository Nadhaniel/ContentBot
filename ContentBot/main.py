import os
from dotenv import load_dotenv
load_dotenv()

from ContentBot.HelperScripts import RedditScraper as rs
from ContentBot.HelperScripts import SqlDatabase as sq
from ContentBot.HelperScripts import TextToAudio as tta

tta.create_audio("", "test_clip.mp3")
#print(test)

