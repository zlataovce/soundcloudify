# soundcloudify
A SoundCloud bulk music downloader

## Installation
 - You can use the prebuilt program in releases or you can compile from source.

## Compiling from source
 - Install soundcloud-lib and pyinstaller with pip.
 - Run the following command in the source directory: pyinstaller --onefile --hidden-import sclib soundcloudify.py
 - Open the dist directory and use the soundcloudify.exe file!

## Usage
 - Make a music.txt file and write the SoundCloud songs URLs to the file (each URL on a new line, no whitespaces, no blank lines).
 - Run the file and let it download the music.
 - Listen to the music in the music directory!
