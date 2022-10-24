#Import module

#import python UI framework - tkinter
from tkinter import *
# import osgeo package 
from osgeo import osr
# import gmplot package 
import gmplot 
# import matplotlib.pyplot package
import matplotlib.pyplot as plt
# import numpy package
import numpy as np


#----------------------------------------------------------------------------------------    
#Create Window
window = Tk()
#Add title 
window.title("GAC MScG10")
#Adjust size of the window
window.geometry("700x650")      



#---------------------------------------------------------------------------------------    
#Set background image
bg = PhotoImage(file='G:\Project\img.png')     
#Define Label for background image
my_lbl = Label(window, image = bg)             
my_lbl.place(x=0, y=0, relwidth=1, relheight=1)


#---------------------------------------------------------------------------------------    
#create frames
frame1=Frame(window, width=295, height= 0,highlightbackground='blue',highlightthickness=2)
frame1.grid(row=0,column=0,padx=10, pady=10, ipadx=5,ipady=5)


#---------------------------------------------------------------------------------------
#define variables

entry_total = []    
global A
generated_CoordinatesArray = []
latitutdeSet = []
longitudeSet = []
lat_set = []
long_set = []

selected = IntVar()
radio_value = IntVar()

mapName = StringVar()


        
#---------------------------------------------------------------------------------------        
#create user-defined functions 1 (Reset the program)
def clear():
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
    txt4.delete(0,END)
    txt5.delete(0,END)
    submit.config(text="Submit",state="normal")
    check.config(state="disable")
    calculate.config (state="disable")
    convert.config (state="disable")
    Generate.config (text="Generate Map", state="disable")
    mplot.config (text="Create Your Scaled Sketch Here", state="normal")
    lbl_step2.config(text="***********************************")
    lbl_step6.config(text="***********************************", fg="grey")
    selected.set(None)

#---------------------------------------------------------------------------------------
#create user-defined functions 2(get "entry set" grid )
def set_point():
    #record user input--(no of corner points of the land)
    m = int(txt1.get())
    #check conditions
    if m>2:
        #output configurations
        submit.config(text="Submitted",state="disable",     
                      font=("Cambria", 11,))
        check.config(state="normal")
        lbl_step1.config(text="Please Enter X,Y Cordinates",
                         font=("Cambria", 10,),
                         fg="black")

        #loop for the number of Rows
        for a in range(m):
            #loop for the number of Columns
            for b in range(2):
                #set the user input data to the variable
                entry_set = Entry(frame1)
                entry_set.grid(row=a, column=b, pady=10, padx=10)
                entry_total.append(entry_set)       

    #check conditions
    else :
        #output configurations
        submit.config(text="Re Submit",font=("Cambria", 11,))   
        lbl_step1.config(text="You Entered Points, Unable to Create a Polygon ",
                         font=("Cambria", 9,),
                         fg="red")



    
#---------------------------------------------------------------------------------------    
#create user-defined functions 3 (insert cordinates to the array )
def add_cordinate():
    #record user input--(no of corner points of the land)
    m = int(txt1.get())
    #Fixed the muliple array parameter
    n=2
    #defined the array
    xy=[]
    for i in range (0,m):
        xy.append([])
    for i in range (0,m):
        for j in range (0,n):
                xy[i].append(j)
                xy[i][j]=0
    #add cordinates to the array           
    for i in range (0,m):
        for j in range(0,n):
            k=i+j+i
            ###print(k)
            xy[i][j]=float(entry_total[k].get())


    #print mmassage & added values
    print('Cordinates of Your Land, You Entered ;')
    print(xy)
    #Call the defined function
    calculate_points(xy)

    #output configurations
    txt2.config (state="normal")
    txt2.insert(0,xy)
    check.config(state="disable")
    calculate.config (state="normal")
    Generate.config (state="normal")
    mplot.config (state="normal")
    lbl_step2.config(text="Cordinates of Your Land, You Entered")

#---------------------------------------------------------------------------------------
#create - user defined function 4 (calculate/traformation of cordinates)
def calculate_points(pointsArray = []):
    global latitutdeSet
    global longitudeSet
    global lat_set
    global long_set
    
    latitutdeSet = []
    longitudeSet = []

    lat_set = []
    long_set = []
    
    for point in pointsArray:
        pointX = point[0]
        pointY = point[1]
        pointZ = 0.0

        #spatial Reference System
        inputEPSG = 5235
        outputEPSG = 4326

        #create coordinate transformation
        inSpatialRef = osr.SpatialReference()
        inSpatialRef.ImportFromEPSG(inputEPSG)

        outSpatialRef = osr.SpatialReference()
        outSpatialRef.ImportFromEPSG(outputEPSG)

        coordTransform = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)

        #transform point, height z is optional
        x, y, z = coordTransform.TransformPoint(pointX, pointY, pointZ)

        #print point in EPSG 4326
        print(x, y)

        #assign output values to the list seperately
        latitutdeSet.append(x)
        longitudeSet.append(y)
        
        lat_set.append(pointX)
        long_set.append(pointY)

    ###matplot(latitudeArray=lat_set,longitudeArray=long_set)
        
    print (lat_set, long_set)
 

#---------------------------------------------------------------------------------------
#create - user defined function 5 (generate scaled sketch)
def matplot():
    global lat_set
    global long_set

    print(lat_set, long_set)

    lat_set.append(lat_set[0])
    long_set.append(long_set[0])


    #plt.plot(X, Y)
    #plt.show()
    if(len(lat_set)==len(long_set)):
        xpoints = np.array(lat_set)
        ypoints = np.array(long_set)
        plt.plot(xpoints, ypoints)
        #named label axes
        plt.xlabel("East Cordinates")
        plt.ylabel("North Cordinates")
        plt.show()

        mplot.config (text="Done! Save Your File from Display Window", state="disable", fg="green")
    
    else:
        print("Array length mismatch")
        
        mplot.config (text="Check Your Cordinates Again",state="normal",fg="red")
    

#---------------------------------------------------------------------------------------
#create - user defined function 6 (generate map html files)
def generate_map_files():
    global latitutdeSet
    global longitudeSet
    print("mapname===",mapName.get())
    mapNameValue = mapName.get()
    if(len(mapNameValue) > 0):
        if(len(latitutdeSet) == len(longitudeSet)):
            print("[OK] Equal Size of Cordinate Arrays/Map Created")
            
            #draw polygon on google map
            latitude_list = latitutdeSet 
            longitude_list = longitudeSet 
            gmap5 = gmplot.GoogleMapPlotter(latitutdeSet[0], longitudeSet[0], 12)  
              
            gmap5.scatter( latitude_list, longitude_list, '#FF0000', size = 40, marker = False) 
              
            # polygon method Draw a polygon with the help of coordinates 
            gmap5.polygon(latitude_list, longitude_list, 
                               color = 'cornflowerblue') 
              
            gmap5.draw(f"{mapNameValue}.html")

            #output configurations
            Generate.config(text="Done",state="disable",     
                        font=("Cambria", 11,))
            lbl_step6.config(text="**Successfully Generated**", fg="green",   
                      font=("Cambria", 11,))          
            
        else:
            print("Missmatch Issue with Entered Cordinate Set")

            Generate.config(text="Try Again",state="normal",     
                      font=("Cambria", 11,))

    else:
        print("Map Name Cannot be Empty ")

        Generate.config(text="Try Again",state="normal",     
                    font=("Cambria", 11,))
        lbl_step6.config(text="**Please Enter a Name to Save Your Map**",
                            font=("Cambria", 9),
                            fg="red")


    
#----------------------------------------------------------------------------------------
#create - user defined function 7 (Calculate the area of defined polygen)
def Calculation():
    #record user input--(no of corner points of the land)
    m = int(txt1.get())
    #Fixed the muliple array parameter
    n=2
    #defined the array
    xy=[]
    
    for i in range (0,m):
        xy.append([])
    for i in range (0,m):
        for j in range (0,n):
                xy[i].append(j)
                xy[i][j]=0

    #add cordinates to the array             
    for i in range (0,m):
        for j in range(0,n):
            k=i+j+i
            ####print(k)
            xy[i][j]=float(entry_total[k].get())

    #print('Cordinates of Your Land, You Entered ;')
    #print(xy)
    
    
    def explode_xy(xy):
        xl=[]
        yl=[]
        #add data to the list  
        for i in range(len(xy)):
            xl.append(xy[i][0])
            yl.append(xy[i][1])
        return xl,yl
        
    def shoelace_area(x_list,y_list):
        #calculation done by shoelace theory
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

    #output configurations
    txt3.insert(0,A)
    lbl_step3.config(text='Area of Your Land (sq.m.);' )
    lbl_step4.config(state="normal" )
    lbl_step6.config(text="**Please Enter a Name to Save Your Map**",
                            font=("Cambria", 9),
                            fg="black")
    calculate.config(state="disable")
    radio_but1.config(state="normal" )
    radio_but2.config(state="normal" )
    radio_but3.config(state="normal" )
    convert.config(state="normal" )


   
#---------------------------------------------------------------------------------------   
#create - user defined function 8 (to convert area)
def convertion():
    
    f_area=float(txt3.get())
    radio_value = selected.get()
    
    if radio_value == 1:
        c1_area=f_area*10.764
        print (c1_area)
        txt4.insert(0,c1_area)

    elif radio_value == 2:
        c2_area=f_area/4047
        print (c2_area)
        txt4.insert(0,c2_area)

    elif radio_value == 3:
        c3_area=f_area/10000
        print (c3_area)
        txt4.insert(0,c3_area)



#----------------------------------------------------------------------------------------
#Lables

lbl_head_line = Label(window, text="-----------------------------",fg="blue",
               font=("Cambria", 22,))
lbl_head_line.place(x=350, y=30)

lbl_heading = Label(window, text="-Geo Area Calculator-", fg="blue",
               font=("Cambria", 23,))
lbl_heading.place(x=350, y=10)

lbl_point_input = Label(window, text="Enter the Number of Points :",
                       font=("Cambria", 12,))
lbl_point_input.place(x=350, y=60)

lbl_point_input_def = Label(window, text="**Please Enter only points, You have the Cordinates**",
                            font=("Cambria", 9),
                            fg="grey")
lbl_point_input_def.place(x=350, y=85)

lbl_step1 = Label(window, text="***********************************",
                  font=("Cambria", 10))
lbl_step1.place(x=350, y=135)

lbl_step2 = Label(window, text="***********************************",
                  font=("Cambria", 10))
lbl_step2.place(x=350, y=195)

lbl_step3 = Label(window, text="***********************************",
                  font=("Cambria", 10))
lbl_step3.place(x=350, y=305)

lbl_step4 = Label(window, text="Select Area Conversion Method", fg="blue",
                  font=("Cambria", 11))
lbl_step4.place(x=350, y=358)

lbl_step5 = Label(window, text="Generate - Map/Scaled Sketch", fg="blue", 
                  font=("Cambria", 12))
lbl_step5.place(x=350, y=500)

lbl_step6 = Label(window, text="***********************************",
                  font=("Cambria", 10))
lbl_step6.place(x=350, y=530)



#----------------------------------------------------------------------------------------
#Entries globaly

txt1 = Entry(window, width=6,font=("Cambria", 14,))
txt1.place(x=570,y=61)
txt1.focus()

txt2 = Entry(window, width=41,state="disable", font=("Cambria", 9,))
txt2.place(x=350,y=215)
txt2.focus()

txt3 = Entry(window, width=11,font=("Cambria", 12,))
txt3.place(x=350,y=325)
txt3.focus()

txt4 = Entry(window, width=22,font=("Cambria", 13,))
txt4.place(x=440,y=465)
txt4.focus()


txt5 = Entry(window, width=20,font=("Cambria", 13,), textvariable=mapName)
txt5.place(x=350,y=550)
txt5.focus()

#----------------------------------------------------------------------------------------
# Create Buttons

# Regular buttons

submit= Button(window, text="Submit",command=set_point,
                   font=("Cambria", 11,))
submit.place(x=350, y=105)


reset= Button(window, text="Reset",command=clear,
                   font=("Cambria", 11,))
reset.place(x=570, y=105)


check= Button(window, text="Check Cordinate Values",state="disable",command=add_cordinate,
                   font=("Cambria", 11,))
check.place(x=350, y=165)


calculate= Button(window, text="Calculate Area", command=Calculation, state="disable",
                    font=("Cambria", 11,))
calculate.place(x=350, y=275)


convert= Button(window, text="Convert >>", command=convertion, state="disable",
                    font=("Cambria", 10,))
convert.place(x=350, y=465)


Generate= Button(window, text="Generate Map", command=generate_map_files, state="disable",
                    font=("Cambria", 10,))
Generate.place(x=550, y=550)

mplot= Button(window, text="Create Your Scaled Sketch Here", command=matplot, state="disable",
                    font=("Cambria", 11,))
mplot.place(x=350, y=590)


# Radio Buttons

radio_but1 = Radiobutton(window, text='Sq.meters to Sq.Foot',value=1, variable=selected,state="disable",
                         font=("Cambria", 11,))
radio_but1.place(x=350, y=375)


radio_but2 = Radiobutton(window, text='Sq.meters to Acres',value=2, variable=selected,state="disable",
                         font=("Cambria", 11,))
radio_but2.place(x=350, y=405)


radio_but3 = Radiobutton(window, text='Sq.meters to Hectares',value=3, variable=selected,state="disable",
                         font=("Cambria", 11,))
radio_but3.place(x=350, y=435)

    
window.mainloop()


