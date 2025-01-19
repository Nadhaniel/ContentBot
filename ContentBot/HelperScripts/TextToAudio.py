import os
import openai
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

fable_wpm = 177
model = 'tts-1'
voice = 'fable'

audio_clips_directory = "../assets/TTS_Clips"

def calculate_cost(text_string):
    cost_tier = {
        'tts-1': 0.015,
        'tts-1-hd': 0.03
    }
    cost_unit = cost_tier.get(model, None)
    if cost_unit is None:
        return None
    return (cost_unit * len(text_string)) / 1000

def calculate_time_of_audio(input_text):
    word_count = len(input_text.split())
    estimated_duration_minutes = word_count / fable_wpm
    estimated_duration_seconds = estimated_duration_minutes * 60

    return (estimated_duration_minutes, estimated_duration_seconds)

def create_audio(text_input_str, file_name):

    audio_length = calculate_time_of_audio(text_input_str)
    cost_estimate = calculate_cost(text_input_str)
    print("Audio length estimated: Minutes - " + str(audio_length[0]) + " Seconds - " + str(audio_length[1]))
    print("Cost to generate: $" + str(cost_estimate))
    print("Do you accept cost of creation (Y/n): ")
    user_accept_cost_flag = str(input())
    if(user_accept_cost_flag == 'Y'):
        try:
            response = client.audio.speech.create(
                model=model,
                input=text_input_str,
                voice=voice
            )
            print("----------Audio generated----------")

            if not(os.path.exists(audio_clips_directory)):
                ValueError("Directory for clip storage does not exist")
            else:
                output_file = os.path.join(audio_clips_directory, file_name)
                response.write_to_file(output_file)

        except openai.OpenAIError as e:
            print("Error generating audio file from OpenAI", e)

    elif(user_accept_cost_flag == 'n'):
        print("No audio file created!")

