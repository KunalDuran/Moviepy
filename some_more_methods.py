from moviepy.editor import VideoFileClip


path = r'F:\moviepy_output\TRIMMED.mp4'
file = VideoFileClip(path)

# CROPPING A RECTANGLE OUT OF A CLIP 
# new = file.crop(x1=50, y1=60, x2=460, y2=275)
# new.write_videofile(r'F:\fasd.mp4')



# FADE-IN AND FADE-OUT
# new = file.fadein(3).fadeout(3)
# new.write_videofile(r'F:\fifo.mp4')



# RESIZE TO NEW RESOLUTION
# new = file.resize( (480,640) )
# new.write_videofile(r'F:\resizinged.mp4')



# TRIMMING VIDEO FILE
# new = file.subclip(t_start=0, t_end=5)
# new.write_videofile(r'F:\TRIMMED.mp4')

# WRITIING GIF FROM VIDEO
# file.write_gif(r'F:\giffed.gif')



# EXTRACT AUDIO
from moviepy.editor import ffmpeg_tools
ffmpeg_tools.ffmpeg_extract_audio(path, output=r'F:\onlyaudio.mp3')
