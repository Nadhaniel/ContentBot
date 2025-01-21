from PIL import Image, ImageDraw, ImageFont
import textwrap

def reddit_thumbnail(path_to_image, path_to_save, subreddit, title):
    image = Image.open(path_to_image)
    draw = ImageDraw.Draw(image)

    subreddit_arial_font = ImageFont.truetype("C:/Users/nadha/PycharmProjects/ContentBot/assets/Fonts/arial/arial/ARIALBD.ttf", size=26)
    title_arial_font = ImageFont.truetype("C:/Users/nadha/PycharmProjects/ContentBot/assets/Fonts/arial/arial/ARIALBD.ttf", size=36)
    subreddit_text_postion = (280, 70)
    title_text_postion = (200, 220)
    text_color = (0, 0 , 0)
    draw.text(subreddit_text_postion, subreddit, fill=text_color, font=subreddit_arial_font)

    max_width = 550
    wrapped_title = textwrap.fill(title, width=40)
    draw.multiline_text(title_text_postion, wrapped_title, fill=text_color, font=title_arial_font, spacing=10)
    image.show()
    print("Save thumbnail (Y/n): ")
    save_image_flag =  str(input())
    if(save_image_flag == 'Y'):
        image.save(path_to_save)
    elif(save_image_flag == 'n'):
        image.close()
    else:
        raise ValueError("[ThumbnailEditor.py][ERROR] - Invalid input from save thumbnail input")
