
from tkinter import *

    
#Create Windows
window = Tk()
window.title("LAC MscG10")
window.geometry("600x700")


#---------------------------------------------------------------------------------
#define variables
entry_total = []
global B
global A
selected = IntVar()

#---------------------------------------------------------------------------------
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
        
#---------------------------------------------------------------------------------        
#create user-defined functions 2 (for reset)
def clear():
    txt1.delete(0,END)
    submit.config(text="Submit",state="normal")
    check.config(state="disable")
    calculate.config (state="disable")
    lbl_step2.config(text="***********************************")

    
#---------------------------------------------------------------------------------    
#create user-defined functions 3 (insert cordinates to the array and calculate area)
def add_cordinate():

    m = int(txt1.get())
    n=2
    xy=[]
    
    for i in range (0,m):
        xy.append([])
    for i in range (0,m):
        for j in range (0,n):
                xy[i].append(j)
                xy[i][j]=0
                
    for i in range (0,m):
        for j in range(0,n):
            k=i+j+i
            print(k)
            xy[i][j]=float(entry_total[k].get())


    
    print('Cordinates of Your Land, You Entered ;')
    print(xy)
    
    txt2.config (state="normal")
    txt2.insert(0,xy)
    check.config(state="disable")
    calculate.config (state="normal")
    lbl_step2.config(text="Cordinates of Your Land, You Entered")

    
#------------------------------------------------------------
def Calculation():

    m = int(txt1.get())
    n=2
    xy=[]
    
    for i in range (0,m):
        xy.append([])
    for i in range (0,m):
        for j in range (0,n):
                xy[i].append(j)
                xy[i][j]=0
                
    for i in range (0,m):
        for j in range(0,n):
            k=i+j+i
            print(k)
            xy[i][j]=float(entry_total[k].get())


    
    print('Cordinates of Your Land, You Entered ;')
    print(xy)
    
    
    def explode_xy(xy):
        xl=[]
        yl=[]
        for i in range(len(xy)):
            xl.append(xy[i][0])
            yl.append(xy[i][1])
        return xl,yl
        
    def shoelace_area(x_list,y_list):
        a1,a2=0,0
        x_list.append(x_list[0])
        y_list.append(y_list[0])
        for j in range(len(x_list)-1):
            a1 += x_list[j]*y_list[j+1]
            a2 += y_list[j]*x_list[j+1]
        l=abs(a1-a2)/2
        return l
    xy_e=explode_xy(xy)

    A=shoelace_area(xy_e[0],xy_e[1])
    print("Total Area is =", A)
    
    txt3.insert(0,A)
    lbl_step3.config(text='Area of Your Land (sq.m.);' )
    lbl_step4.config(state="normal" )
    calculate.config(state="disable")
    radio_but1.config(state="normal" )
    radio_but2.config(state="normal" )
    radio_but3.config(state="normal" )
    convert.config(state="normal" )


    
def test():
    #B=txt2.get()
    area1=float(txt3.get())
    #print B
    print (area1*2)
    

#----------------------------------------------------------------------------------
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
                            fg="grey")
lbl_point_input_def.place(x=300, y=85)

lbl_step1 = Label(window, text="***********************************",
                  font=("Cambria", 10))
lbl_step1.place(x=300, y=135)

lbl_step2 = Label(window, text="***********************************",
                  font=("Cambria", 10))
lbl_step2.place(x=300, y=195)

lbl_step3 = Label(window, text="***********************************",
                  font=("Cambria", 10))
lbl_step3.place(x=300, y=305)

lbl_step4 = Label(window, text="Please Select Area Conversion Method",
                  font=("Cambria", 10))
lbl_step4.place(x=300, y=360)

#lbl_step3.config(text=xy, fg="Black" )

#-----------------------------------------------------------------------------------
#Entries globaly

txt1 = Entry(window, width=6,font=("Cambria", 14,))
txt1.place(x=520,y=61)
txt1.focus()

txt2 = Entry(window, width=41, state="disable", font=("Cambria", 9,))
txt2.place(x=300,y=215)
txt2.focus()

txt3 = Entry(window, width=11,font=("Cambria", 12,))
txt3.place(x=300,y=325)
txt3.focus()

txt4 = Entry(window, width=10,font=("Cambria", 13,))
txt4.place(x=390,y=465)
txt4.focus()

#-----------------------------------------------------------------------------------
# Create Buttons

# Regular buttons

submit= Button(window, text="Submit",command=set_point,
                   font=("Cambria", 11,))
submit.place(x=300, y=105)

reset= Button(window, text="Reset",command=clear,
                   font=("Cambria", 11,))
reset.place(x=520, y=105)


check= Button(window, text="Check Cordinate Values",state="disable",command=add_cordinate,
                   font=("Cambria", 11,))
check.place(x=300, y=165)

calculate= Button(window, text="Calculate Area", command=Calculation, state="disable",
                    font=("Cambria", 11,))
calculate.place(x=300, y=275)

convert= Button(window, text="Convert >>", command=test, state="disable",
                    font=("Cambria", 10,))
convert.place(x=300, y=465)


# Radio Buttons

radio_but1 = Radiobutton(window, text='Sq.meters to Sq.kilometers',value=1, variable=selected,state="disable",
                         font=("Cambria", 11,))
radio_but1.place(x=300, y=375)

radio_but2 = Radiobutton(window, text='Sq.meters to Hectares',value=2, variable=selected,state="disable",
                         font=("Cambria", 11,))
radio_but2.place(x=300, y=405)

radio_but3 = Radiobutton(window, text='Sq.meters to Acres',value=3, variable=selected,state="disable",
                         font=("Cambria", 11,))
radio_but3.place(x=300, y=435)

    
window.mainloop()


