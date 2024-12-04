from tkinter import*

window = Tk()                           #this will create a window instance | Tk() is a class
window.geometry('320x320')             #resizing window
window.title('My 1st GUI window!')    #renaming title window

label = Label(window,text='How are you?')   # text labeling
label.place(x=50,y=100)                     #position label

window.mainloop()                       #this will display the window