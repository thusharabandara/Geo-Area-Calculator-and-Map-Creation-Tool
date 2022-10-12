
from tkinter import *

#define array
entry_total = []
    
#create user-defined functions 1(get entry set grid & create some status)
def set_point():       
    m = int(txt1.get())
    if m>2:
        submit.config(text="Submitted",state="disable",
                      font=("Cambria", 11,))
        check.config(state="normal")
        lbl_step1.config(text="Please Enter X,Y Cordinates",
                         font=("Cambria", 10,),
                         fg="black")
        #Row Loop
        for a in range(m):
            #Column Loop
            for b in range(2):
                entry_set = Entry(window)
                entry_set.grid(row=a, column=b, pady=10, padx=10)
                entry_total.append(entry_set)
    else :
        submit.config(text="Re Submit",font=("Cambria", 11,))
        lbl_step1.config(text="You Entered Points, Unable to Create a Polygon ",
                         font=("Cambria", 9,),
                         fg="red")
        
#create user-defined functions 2 (for reset)
def clear():
    txt1.delete(0,END)
    submit.config(text="Submit",state="normal")
    check.config(state="disable")
    calculate.config (state="disable")
    lbl_step1.config(text="***********************************")
    
    
#Create Windows

window = Tk()
window.title("LAC MscG10")


#Lables
lbl_heading = Label(window, text="-----------------------------",
               font=("Cambria", 22,))
lbl_heading.place(x=300, y=30)

lbl_heading = Label(window, text="-Land Area Calculator-",
               font=("Cambria", 23,))
lbl_heading.place(x=300, y=10)

lbl_point_input = Label(window, text="Enter the Number of Points :",
                       font=("Cambria", 12,))
lbl_point_input.place(x=300, y=60)

lbl_point_input_def = Label(window, text="**Please Enter only points, You have the Cordinates**",
                            font=("Cambria", 9),
                            fg="grey",)
lbl_point_input_def.place(x=300, y=85)

lbl_step1 = Label(window, text="***********************************",
                  font=("Cambria", 9))
lbl_step1.place(x=300, y=135)

lbl_step2 = Label(window, text="***********************************",
                  font=("Cambria", 9))
lbl_step2.place(x=300, y=195)

#Entries

txt1 = Entry(window, width=6,font=("Cambria", 14,))
txt1.place(x=520,y=61)
txt1.focus()

# Create Buttons

# Regular button

submit= Button(window, text="Submit",command=set_point,
                   font=("Cambria", 11,))
submit.place(x=300, y=105)

reset= Button(window, text="Reset",command=clear,
                   font=("Cambria", 11,))
reset.place(x=520, y=105)


check= Button(window, text="Check Cordinate Values",state="disable",command=set_point,
                   font=("Cambria", 11,))
check.place(x=300, y=165)

calculate= Button(window, text="Calculate Area",state="disable",command=set_point,
                   font=("Cambria", 11,))
calculate.place(x=300, y=225)


# window size define
window.geometry("600x700")


    
window.mainloop()


