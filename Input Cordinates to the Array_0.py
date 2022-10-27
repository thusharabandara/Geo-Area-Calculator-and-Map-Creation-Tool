
from tkinter import *

#Create Windows

window = Tk()
window.title("LAC MscG10")
window.geometry("700x500")

my_entries = []
def something():
    entry_list = ''
    
    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) 
        my_label.config(text=entry_list)

    print(my_entries[2].get())

for y in range(5):
    for x in range(5):
        my_entry = Entry(window)
        my_entry.grid(row=y, column=x ,pady=20, padx=5)
        my_entries.append(my_entry)


my_button=Button(window,text="click me!",command=something)
my_button.grid(row=6, column=0 ,pady=20, padx=5)

my_label=Label(window, text="")
my_label.grid(row=7, column=0, pady=20)

window.mainloop()
