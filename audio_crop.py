from moviepy.editor import AudioFileClip


path = r'____'

file = AudioFileClip(path)


new = file.set_duration((53, 50))

new.write_audiofile(r'H:\short.mp3')


# Above code helps to trim or crop the audio files


