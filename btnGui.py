from tkinter import*

def click():
    print('I am fine!')


window = Tk()                           #this will create a window instance | Tk() is a class
window.geometry('320x320')             #resizing window
window.title('My 1st Button GUI')    #renaming title window

label = Label(window,text='How are you?')   # text labeling
label.place(x=50,y=100)                     #position label

button = Button(window,text='Fine', command=click)
button.place(x=150, y=100)

window.mainloop()                       #this will display the window