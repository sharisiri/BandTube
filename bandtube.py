import questionary
from bs4 import BeautifulSoup
import requests
import subprocess
import os
from rich.console import Console

audio_files_res = []

# Iterate over audio file directory
for file in os.listdir('.'):
    if file.endswith(".mp3"):
        # add file to list
        audio_files_res.append(file)

img_files_res = []

# Iterate over image fille directory
for file in os.listdir('.'):
    if file.endswith(".jpeg") or file.endswith(".png"):
        # add file to list
        img_files_res.append(file)

audiofile = questionary.select(
    "Which track do you want to upload?",
    choices=audio_files_res).ask()

url = questionary.text(
    "Enter the track Bandcamp URL").ask()

title = audiofile.replace('.mp3', '')

confirm_title = questionary.confirm(
    f'Title: {title}', auto_enter=False).ask()

if not confirm_title:
    title = questionary.text(
        "Track Title").ask()

confirm_image = questionary.confirm(
    "Do you want to use the Bandcamp cover image?", auto_enter=False).ask()

if not confirm_image:
    img = questionary.select(
        "Cover Image (png or jpeg)", choices=img_files_res).ask()


# Run BeautifulSoup to get the album cover image.
if confirm_image:
    html = requests.get(url)  # get the html
    # Give the html to BeautifulSoup
    soup = BeautifulSoup(html.text, 'html.parser')

    # Get all the anchor links with the custom class
    # The element or the class name will change based on your case
    div = soup.find('a', {"class": "popupImage"})
    imgUrl = div.find('img').attrs['src']
    title = audiofile.replace('.mp3', '')
    img = title + '.jpeg'
    wget = ['wget', '-q', imgUrl, '-O', img]
    wget_process = subprocess.Popen(wget)  # Runs wget on input values.
    wget_process.wait()

# Update the ffmpeg command to suit your needs before running the script.
ffmpeg = [
    'ffmpeg',
    "-v", "quiet",
    '-loop', '1',
    '-i', img,
    '-i', audiofile,
    f'{title}.mp4'
]

ffmpeg_process = subprocess.Popen(ffmpeg)

console = Console()

with console.status("[bold green]Generating mp4 file...") as status:
    while ffmpeg_process.wait():
        sleep(1)
        status.update("[bold green]Generating mp4 file...")

upload = ['python3',
          'upload_video.py',
          '--file', f'{title}.mp4',
          '--title', title,
          '--description',
          f'''Add your description here.
          
          It can be multiple lines.
          ''',
          '--category', '10',
          '--privacyStatus', 'unlisted']

upload_process = subprocess.Popen(upload)
upload_process.wait()
