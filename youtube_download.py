from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading.')

ydl_sample = {
    'format': 'InsertFormatHere',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        '   ': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
'''
Formats: (Separate with commas for multiple files, '/' for more options if main is not available
    (File Ext) 3gp, aac, flv, m4a, mp3, mp4, ogg, wav, webm
    (Video+Audio) best, worst
    (Video only) bestvideo, worstvideo
    (Audio Only) bestaudio, worstaudio
'''

ydl_both = {
    'format': 'best',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
ydl_vid = {
    'format': 'bestvideo/best',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
ydl_aud = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        '   ': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

while True:
    file_type = input("A for Audio, V for Video, B for Both\n\t")
    if file_type.lower() == 'a':
        ydl_opts = ydl_aud
        break
    elif file_type.lower() == 'v':
        ydl_opts = ydl_vid
        break
    elif file_type.lower() == 'b':
        ydl_opts = ydl_both
        break

print(ydl_opts)
link = input("Insert Link:\n\t")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
    
