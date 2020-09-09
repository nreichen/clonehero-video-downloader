# CloneHeroVideoDownloader
Short python script that allows you to download the the top YouTube music video for songs in your Clone Hero library.

Disclaimer
-this is my first github repository so please message me with any feedback on how I can improve upon my work or the way I uploaded my work! :)

REQUIREMENTS
-Must have youtube-dl downloaded (https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme)


PROCEDURE
1. Change the homeFolder to the directory that contains individual song folders--these are the songs that the program will download videos inside.
   For instance, if I want to download videos for all the songs in my Guitar Hero 3 folder, I would change line 17 to 
   homeFolder = "clonehero-win64\Songs\Guitar Hero 3"
2. Run the program.  If the homeFolder exists, the top result on YouTube will be downloaded as an .mp4 into the song folder,
   if the homeFolder doesn't exist, try again with the correct path.
