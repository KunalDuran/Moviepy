from tkinter import *
from moviepy.editor import VideoFileClip
from datetime import datetime


def trim(path, output_path, start, end):
    start, end = tuple(float(i) for i in start.split(',')), tuple(float(i) for i in end.split(','))
    file = VideoFileClip(path)
    new = file.subclip(t_start=start, t_end=end)
    new.write_videofile(output_path)


def dothis():
    input_file = entry_field.get()
    output_file = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".mp4"
    print('Editing: ', operation.get(), input_file, "\n Saving it to " , output_file)
    
    
    if operation.get() == "Trim": 
        start = Entry(root, width=50)
        start.pack()
        start.insert(0, 'Start')
        end = Entry(root, width=50)
        end.pack()
        end.insert(0, 'Input like this-> minutes, seconds')
        edit = Button(root ,text='Edit', command=lambda: trim(input_file, output_file, start.get(), end.get()))
        edit.pack(side=BOTTOM)
    	


root = Tk()
root.geometry('570x350')
root.title('Moviepy Editor GUI')


entry_field = Entry(root, font =5)
entry_field.pack()


#entry_field2 = Entry(root, font =5)
#entry_field2.pack()


entry_field.insert(0, "Path to input file")
# entry_field2.insert(1, "Path to output file")

options = ['Trim', 'Combine']
operation = StringVar()
operation.set(options[0])
drop = OptionMenu(root, operation, *options)
drop.pack()


button1 = Button(root ,text='Convert', command=dothis)
button1.pack(side=BOTTOM)


root.mainloop()





