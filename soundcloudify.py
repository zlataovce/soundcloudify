from sclib import SoundcloudAPI, Track
from os.path import exists
from os import mkdir
from sys import exit, argv
import time

apikey = SoundcloudAPI()


def get_music(url, api, music_folder):
    track = api.resolve(url)

    assert type(track) is Track

    filename = f'./{music_folder}/{track.artist} - {track.title}.mp3'
    properties = f'{track.artist} - {track.title}'
    print("Identified the song: " + properties)

    if exists(filename):
        print("Skipping " + properties + ": The file already exists.")
        return

    with open(filename, 'wb+') as fp:
        try:
            track.write_mp3_to(fp)
            print("Received " + properties + "!")
        except (TypeError, ValueError):
            print("Failed to get " + properties + ".")


if __name__ == '__main__':
    print("SoundCloudify build dev1.1")
    print("---------------------------")
    try:
        path_musicfile = argv[1]
    except IndexError:
        path_musicfile = "music.txt"
    try:
        path_musicfolder = argv[2]
    except IndexError:
        path_musicfolder = "music"
    if not exists(path_musicfldr): mkdir(path_musicfldr)
    if not exists(path_musicfile):
        print("The path doesn't exist. Exiting...")
        time.sleep(2)
        exit()

    with open("music.txt") as file:
        for line in file:
            stripped_line = line.rstrip('\n')
            if 'soundcloud.com' in linestrip:
                get_music(stripped_line, api_key, path_musicfolder)
            else:
                print("Skipping a line: Line doesn't contain a SoundCloud URL.")

    print("Iterated through the file! Music should be downloaded.")
    time.sleep(3)
    exit()
