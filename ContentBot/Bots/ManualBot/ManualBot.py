#Required at start to load environement variables
import dotenv
dotenv.load_dotenv()
import ContentBot.HelperScripts.RedditScraper as rs
import ContentBot.HelperScripts.TextToAudio as tta
import ContentBot.HelperScripts.TikTokFormatter as formatter
import ContentBot.HelperScripts.ThumbnailEditor as te



submissions = rs.get_top_month_submissions(31)
print("-------------Submissions Retrieved-------------")

i = 0
for submission in submissions:
    print("Submission " + str(i))
    print("Title: " + submission["Title"])
    print("Body: " + submission["Body"] + "\n")
    i += 1

#print("Pick a submission")
#submission_number_input = int(input())

final_tts_text = ""
te.reddit_thumbnail("../../../assets/RedditTemplateImage.png", "../../../assets/RedditTemplateImage_edited.png", "r/relationship_advice", "I M23 sustained an injury that will prevent me from having sex for a while my 22F girlfriend wants to open our relationship until I recover, is it time to end it? ")
#tta.calculate_time_of_audio(submissions[submission_number_input][""])
#tta.create_audio(submissions[1]["Body"], "test_submission.mp3", "../../../assets/TTS_Clips")



