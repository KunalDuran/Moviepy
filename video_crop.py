from moviepy.editor import VideoFileClip

# declaring path to the file/video in your machine 
path = r'D:\for_youtube_vids\pip.mkv'

# opening the file and storing it in 'file' variable
file = VideoFileClip(path)

# making a trimmed clip of original video
new = file.subclip(t_start=2, t_end=(2, 55))

# exporting the trimmed video to desired path 
new.write_videofile(r'F:\trimmed.mp4')


# you can experiment with the file formats of output file(this package support most of the common formats)
