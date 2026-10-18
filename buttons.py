#import everything from tkinter module
from tkinter import *

# create a tkinker window
window = Tk()

#open window having dimension 100x100
window.geometry('100x100')

#createbutton
button = Button(window, text='Click me!',bd='5',background="cyan",command=window.destroy )
button1 = Button(window, text='Click me!',bd='5',background="green",command=window.destroy )

#Set the position of button on the top of window.
#try side = bottom, right, left

button.pack(side='right')
button1.pack(side='top')

window.mainloop()