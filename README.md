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

## Options
 - You can specify a location of the txt file with the URLs and the folder where to download in the arguments.
 - Example: soundcloudify.exe mymusic.txt downloads
 - The txt file must be the first argument and the folder must be the second.

## Contribution
 - If you know any fixes/improvements, I suggest that you make a pull request with the changes. I will review the changes and approve/deny them.
 - If you have a feature suggestion, create an issue and specify it.
