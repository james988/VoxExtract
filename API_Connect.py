# This code download YouTube video and after extract the .wav file
import os
import sys
import string
import configparser

from datetime import date
from pytube import YouTube
from moviepy.editor import VideoFileClip

def path_url():
    arq = configparser.RawConfigParser()
    arq.read('config.txt')

    # Get the video link and save path
    video_url  =  arq.get('URLS','url')
    save_path  = arq.get('Path','save_path')
    vocal_path = arq.get('Path', 'vocal_path')

    today_date = date.today().strftime('%d%m%Y')

    sub_save_path = save_path + today_date + '/'
    sub_vocal_path = vocal_path + today_date + '/'
    print('Link and Path were collected\n')
    
    return video_url, sub_save_path, sub_vocal_path

def aud_ext(sub_save_path, rename_filename):  # Extract .wav file from a .mp4 or 3gp file  
    video_path  = os.path.join(sub_save_path, f'{rename_filename}') 
    output_path = os.path.join(sub_save_path, f'{rename_filename[:-5]}.wav')

    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path, codec='pcm_s16le')
    
def API():
    video_url, sub_save_path, vocal_path = path_url()
    print('File Downloading.....\n')

    youtube = YouTube(video_url)

    stream  = youtube.streams.first()

    try:
        stream.download(sub_save_path)

    except ConnectionResetError as error:
        print(error)
        print('The connection failled')
        sys.exit()

    print('The video was downloaded')

    #Rename the downloaded file
    original_filename = stream.default_filename
    
    # Remove any problematic characters from the video title
    ## First cleaning step
    valid_chars       = "-.’'_() %s%s" % (string.ascii_letters, string.digits)
    original_filename = ''.join(c for c in original_filename if c in valid_chars)
    new_filename      = original_filename.replace(" ","")

    ## Second step
    valid_chars = "_. %s%s" % (string.ascii_letters, string.digits)
    new_filename = ''.join(c for c in new_filename if c in valid_chars)

    rename_filename = original_filename.replace(original_filename, new_filename)

    rename_filename = os.path.join(sub_save_path, rename_filename)
    original_save   = os.path.join(sub_save_path, original_filename)

    os.rename(original_save,  rename_filename)

    print('\nThe file was renamed and The Audio extraction starts\n')
    aud_ext(sub_save_path, rename_filename)

    return rename_filename, sub_save_path, vocal_path


if __name__ == '__main__':
    API()