from moviepy.editor import VideoFileClip

path = r'D:\for_youtube_vids\pip.mkv'

file = VideoFileClip(path)

new = file.subclip(t_start=2, t_end=(2, 55))

new.write_videofile(r'F:\trimmed.mp4')
