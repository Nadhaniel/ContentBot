from moviepy.editor import VideoFileClip
from moviepy.video.fx import crop as cp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def extract_clip(input_path, output_path, starting_time, ending_time):
    with VideoFileClip(input_path) as video:
        new = video.subclip(starting_time, ending_time)
        new.write_videofile(output_path, audio_codec=False, preset="veryslow")


def convert_to_tiktok_format(input_path, output_path):
    # Load the video
    clip = VideoFileClip(input_path)

    # Define TikTok's preferred dimensions and aspect ratio
    tiktok_width = 1080
    tiktok_height = 1920
    target_aspect_ratio = tiktok_width / tiktok_height

    # Calculate the current aspect ratio
    original_aspect_ratio = clip.w / clip.h

    # Resize and crop or pad the video
    if original_aspect_ratio > target_aspect_ratio:
        # If the video is too wide, crop the sides
        new_width = int(target_aspect_ratio * clip.h)
        clip = cp.crop(clip, width=new_width, height=clip.h, x_center=clip.w / 2)
    else:
        # If the video is too tall, crop the top and bottom
        new_height = int(clip.w / target_aspect_ratio)
        clip = cp.crop(clip, width=clip.w, height=new_height, y_center=clip.h / 2)

    # Resize the video to 1080x1920
    clip = clip.resize((tiktok_width, tiktok_height))

    # Export the video
    clip.write_videofile(output_path, codec="libx264", fps=30, preset="veryslow")


