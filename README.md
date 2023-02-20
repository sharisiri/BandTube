# BandTube CLI
A CLI tool that converts Bandcamp audio and image files to mp4 videos and uploads them to Youtube in one go.

It uses the following packages: 

- [questionary](https://github.com/tmbo/questionary) to parse arguments.
- [FFMPEG](https://github.com/FFmpeg/FFmpeg) to generate mp4 files.
- [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) to scrape cover images from Bandcamp.
- [The Youtube Data API](https://developers.google.com/youtube/v3) to upload videos.


### Prerequisites
- The wrapper requires a local FFMPEG installation.
- Your app needs to be registered on your GCP console for API authentification. Put the credentials file in the root folder.


### To run
- Edit the FFMPEG command in bandtube.py to suit your needs before running the script.
- Put your audio files in the source directory and run:

```
python3 bandtube.py
```
