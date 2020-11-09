from sclib import SoundcloudAPI, Track
from os.path import exists
from os import mkdir
from sys import exit, argv
import time

apikey = SoundcloudAPI()


def get_music(url, api, musicfldr):
    track = api.resolve(url)

    assert type(track) is Track

    filename = f'./{musicfldr}/{track.artist} - {track.title}.mp3'
    props = f'{track.artist} - {track.title}'
    print("Identified the song: " + props)

    if exists(filename):
        print("Skipping " + props + ": The file already exists.")
        return

    with open(filename, 'wb+') as fp:
        try:
            track.write_mp3_to(fp)
            print("Received " + props + "!")
        except (TypeError, ValueError):
            print("Failed to get " + props + ".")


if __name__ == '__main__':
    print("SoundCloudify build 1.0dev5")
    print("---------------------------")
    try:
        path_musicfile = argv[0]
    except IndexError:
        path_musicfile = "music.txt"
    try:
        path_musicfldr = argv[1]
    except IndexError:
        path_musicfldr = "music"
    if not exists(path_musicfldr):
        mkdir(path_musicfldr)
    if not exists(path_musicfile):
        print("The path doesn't exist. Exiting...")
        time.sleep(2)
        exit()

    with open("music.txt") as file:
        for line in file:
            linestrip = line.rstrip('\n')
            if 'soundcloud.com' in linestrip:
                get_music(linestrip, apikey, path_musicfldr)
            else:
                print("Skipping a line: Line doesn't contain a SoundCloud URL.")

    print("Iterated through the file! Music should be downloaded.")
    time.sleep(3)
    exit()
