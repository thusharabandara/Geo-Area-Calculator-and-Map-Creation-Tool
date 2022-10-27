
from tkinter import *

#Create Windows

window = Tk()
window.title("LAC MscG10")
window.geometry("700x500")

my_entries = []
def something():
      
    m=3
    n=2
    xy=[]
    for i in range (0,m):
        xy.append([])
    for i in range (0,m):
        for j in range (0,n):
                xy[i].append(j)
                xy[i][j]=0
                
    #for k in range(0,6):
        #print(k)
    for i in range (0,3):
        for j in range(0,2):
            k=i+j+i
            print(k)
            xy[i][j]=int(my_entries[k].get())
        
    print('Cordinates of Your Land, You Entered ;')
    print(xy)

for y in range(3):
    for x in range(2):
        my_entry = Entry(window)
        my_entry.grid(row=y, column=x ,pady=20, padx=5)
        my_entries.append(my_entry)


my_button=Button(window,text="click me!",command=something)
my_button.grid(row=6, column=0 ,pady=20, padx=5)

my_label=Label(window, text="")
my_label.grid(row=7, column=0, pady=20)

window.mainloop()
