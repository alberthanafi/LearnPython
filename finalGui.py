from tkinter import*

def submit():
    value = entry.get()
    print(value)

window = Tk()
window.geometry('300x200')
window.title('My 1st Entry Box GUI')

label = Label(window,text='How are you?')   # text labeling
label.place(x=100,y=20)

entry = Entry(window)
entry.place(x=80,y=50)

buttonSubmit = Button(window,text='Submit', command=submit)
buttonSubmit.place(x=120,y=80)

window.mainloop()