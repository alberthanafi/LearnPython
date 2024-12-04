from tkinter import*

def submit():
    valueName = entryName.get()
    valueAge = entryAge.get()

    print(valueName.upper())
    print(valueAge)

window = Tk()
window.geometry('300x200')
window.title('Name & Age')

label = Label(window,text='Your Name: ')   # text labeling
label.place(x=20,y=20)

label = Label(window,text='Your Age: ')   # text labeling
label.place(x=20,y=50)

entryName = Entry(window)
entryName.place(x=100,y=20)

entryAge = Entry(window)
entryAge.place(x=100,y=50)

buttonSubmit = Button(window,text='Submit', command=submit)
buttonSubmit.place(x=120,y=80)

window.mainloop()