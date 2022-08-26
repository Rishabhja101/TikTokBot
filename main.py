import requests
from gtts import gTTS
import os
import moviepy.editor as mp
import moviepy as mpy
import random
import math

language = 'en'

# Reddit authentication
client_id = 'b-62hjVEwKOQ8KL6_l0GCQ'
secret_token = 'VrI1N42e-TLtt7HWoLioxAYm1oOtSw'
auth = requests.auth.HTTPBasicAuth(client_id, secret_token)
data = {'grant_type': 'password',
        'username': 'TDZ6',
        'password': 'P6NRTARHcqqAf6@k'}
headers = {'User-Agent': 'CoqueBot/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)


# Reddit data request
res = requests.get("https://oauth.reddit.com/r/AmItheAsshole/hot",
                   headers=headers)
selftext = res.json()['data']['children'][1]['data']['selftext']


# generate TTS
myobj = gTTS(text=selftext, lang=language, slow=False)
myobj.save("audio.mp3")
audio = mp.AudioFileClip('audio.mp3')

# generate random video clip with 9:16 ratio
video = mp.VideoFileClip('video_original.mp4')
audio_duration = int(math.ceil(audio.duration))
end = random.randrange(audio_duration + 5, int(math.ceil(video.duration)))
start = end - audio_duration
clip = video.subclip(start, end)

# crop
offset = 437
width = 406
cropped_video = mpy.video.fx.all.crop(clip, x1=offset, width=width)

# save final video
final_video = cropped_video.set_audio(audio)
final_video.write_videofile('output_video.mp4')

os.remove("audio.mp3")


