from pytube import YouTube
from openai import OpenAI



def transcribeVideo(ytVideo):
    audio = ytVideo.streams.filter(only_audio = True).all()
    audio_file = audio.download()
  
youtubeLink = input("Enter your link!") #Prompt user for input
print("\n")

try: #Exception handling
    video = YouTube(youtubeLink)
    transcribeVideo(video)
except Exception as error: #Exception handling
    print("Failed to retrieve video. Please try again.", error)

