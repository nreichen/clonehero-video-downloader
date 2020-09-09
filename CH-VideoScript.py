#import youtube-dl
from __future__ import unicode_literals
import youtube_dl

#import PyUsb
import usb

#import google search
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

import os 


homeFolder = "D:\clonehero-win64\Songs\The Beatles (Various Songs)"
os.chdir(homeFolder)
print(os.getcwd())


for file in os.listdir():
	query = 'Youtube {} (Official Music Video)'.format(file)

	#scrapes the URL from google
	for j in search(query, tld="com", lang='en', num=1, start=0, stop=1):
		url = j;

	#changes the download folder
	currentSongFileFolder = '{}/{}'.format(homeFolder, file)
	os.chdir(currentSongFileFolder)

	#downloads the song in the correct folder
	#IN THE FUTURE ADD 'format': 'bestaudio/best' TO ydl_opts (so that quality can be improved)
	ydl_opts = {'outtmpl': 'video.mp4',
				'nooverwrites': 0,
				'noplaylist': 1}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([url])
	

