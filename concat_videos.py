from moviepy.editor import VideoFileClip, concatenate_videoclips

path = input('Enter file path : ')
path2 = input('Enter second file path : ')

clip1 = VideoFileClip(path)

clip2 = VideoFileClip(path2)

final = concatenate_videoclips([clip1,clip2])

destination = input('Where you want to save your file')

final.write_videofile(destination)