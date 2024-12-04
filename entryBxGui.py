from tkinter import*

def submit():
    value = entry.get()
    print(value)

window = Tk()
window.geometry('320x320')
window.title('My 1st Entry Box GUI')

entry = Entry(window)
entry.place(x=150,y=50)

buttonSubmit = Button(window,text='Submit', command=submit)
buttonSubmit.place(x=150,y=100)

window.mainloop()