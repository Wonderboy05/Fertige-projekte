#!/user/bin/env python3

from pytube import YouTube
def on_complete(stream, filepath):
	print('Download fertig')
	print(filepath)

def on_progress(stream, chunk, bytes_remainig):
	progress_string = f'{round(100 - (bytes_remainig / stream.filesize * 100),2)}%'
	print(progress_string)

link = input('YouTube link: ')
video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

print(f'title: 	{video_object.title}')
print(f'length: {round(video_object.length / 60,2)} minutes')
print(f'author: {video_object.author}')

print('download: (b)est | (m)ittel | (v)verlassen')
download_choice = input('choice: ')

match download_choice:
	case 'b':
		video_object.streams.get_highest_resolution().download(r'C:\Users\basti\Downloads')
	case 'm':
		video_object.streams.get_lowest_resolution().download(r'C:\Users\basti\Downloads')

