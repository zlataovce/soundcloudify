from sclib import SoundcloudAPI, Track, Playlist
import os
from sys import exit
import time

api = SoundcloudAPI()

def get_music(url, api):
    track = api.resolve(url)
    
    assert type(track) is Track
        
    filename = f'./music/{track.artist} - {track.title}.mp3'
    props = f'{track.artist} - {track.title}'
    print("Identified the song: " + props)

    if os.path.exists(filename):
        print("Skipping " + props + ": The file already exists.")
        return
    
    with open(filename, 'wb+') as fp:
        try:
            track.write_mp3_to(fp)
            print("Received " + props + "!")
        except:
            print("Failed to get " + props + ".")

print("SoundCloudify build 1.0dev2")
print("---------------------------")
if not os.path.exists("music"):
    os.mkdir("music")
if not os.path.exists("music.txt"):
    print("The music.txt doesn't exist. Exiting...")
    time.sleep(2)
    exit()

with open("music.txt") as file:
    for line in file:
        get_music(line.rstrip('\n'), api)

print("Iterated through the file! Music should be downloaded.")
time.sleep(3)
exit()
        
