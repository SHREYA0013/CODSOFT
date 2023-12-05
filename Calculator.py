# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 21:00:56 2023

@author: shreya
"""
#Building GUI Calculator:
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import Button, Frame, LEFT, StringVar

#messagebox.NameoftheFunction(title,message,**options)
#Calculator structure contains Labels,Frames,Buttons(widgets);

#Function that will operate the working of buttons:
var="" #setting initial values
A=0
operator=""

def button_1_is_clicked():   
    global var
    var=var+"1"
    the_data.set(var)
#I define some vriables and initialize them with some initial values. Whenever the user press 1,this function will generate.then I define 'global' keyword too. this allows us to modify the variable inside the function.
#Concatinate 1 to the variable and set StringVar using set().
#whenever the user  press 1,this function will be called.Store it in a different variable to make the calculation easier.

def button_2_is_clicked():   
    global var
    var=var+"2"
    the_data.set(var) #defining function for button 2
    
def button_3_is_clicked():
    global var
    var=var+"3"
    the_data.set(var) #defining function for button 3
    
def button_4_is_clicked():   
    global var
    var=var+"4"
    the_data.set(var) #defining function for button 4
    
def button_5_is_clicked():   
    global var
    var=var+"5"
    the_data.set(var) #defining function for button 5  
    
def button_6_is_clicked():   
    global var
    var=var+"6"
    the_data.set(var) #defining function for button 6    
    
def button_7_is_clicked():   
    global var
    var=var+"7"
    the_data.set(var) #defining function for button 7
    
def button_8_is_clicked():   
    global var
    var=var+"8"
    the_data.set(var) #defining function for button 8
    
def button_9_is_clicked():   
    global var
    var=var+"9"
    the_data.set(var) #defining function for button 9
    
def button_0_is_clicked():   
    global var
    var=var+"0"
    the_data.set(var) #defining function for button 0
    
def button_add_is_clicked():  
    global A
    global var
    global operator
    A=float(var)
    operator="+"
    var=var+"+"
    the_data.set(var) #defining function for button +
    
def button_sub_is_clicked():  
    global A
    global var
    global operator
    A=float(var)
    operator="-"
    var=var+"-"
    the_data.set(var) #defining function for button -
    
def button_mul_is_clicked():  
    global A
    global var
    global operator
    A=float(var)
    operator="*"
    var=var+"*"
    the_data.set(var) #defining function for button *  
    
def button_div_is_clicked():  
    global A
    global var
    global operator
    A=float(var)
    operator="/"
    var=var+"/"
    the_data.set(var) #defining function for button /
    
def button_equal_is_clicked():  
    global A
    global var
    global operator
    var2=var
    
    try:
        result=eval(var2)
        the_data.set(result)
    except Exception as e:
        the_data.set("error")#defining function for button =
    
def button_clr_is_clicked():  
    global A
    global var
    global operator
    var=""
    A=0
    operator=""
    the_data.set(var) #defining function for button Clear
    
#define function to display function:

def result():
    global A
    global operator
    global var
    var2=var
    
    if operator=="+":
        p=float((var2.split("+")[1]))
        x=A+p
        the_data.set(x)
        var=str(x)
    elif operator=="-":
        p=float((var2.split("-")[1]))
        x=A-p
        the_data.set(x)
        var=str(x)
    elif operator=="*":
        p=float((var2.split("*")[1]))
        x=A*p
        the_data.set(x)
        var=str(x)
    elif operator=="/":
        p=float((var2.split("/")[1]))
        if p==0:
            messagebox.showerror("Can't operate division by 0")
            A==""
            var=""
            the_data.set(var)
        else:
            x=float(A/p)
            the_data.set(x)
            var=str(x)
#till now we append the required value or operator to the string. values ranging from 0-9,and 4 operators along with equal and clear sign.
#We used global keyword to modify values. 

#Now we will create the window for our Calculator:
#Tkinter library helps us to create window consisting title bar and frames and other decorations.
#Window consists of Title bar and borders.Then we can add other widgets.
        
GUI_Window= tkinter.Tk() #creating object
GUI_Window.geometry("320x600+400+400") #size of the window
GUI_Window.resizable(0,0) #desable the resize option for better UI
GUI_Window.title("GUI CALCULATOR")

#Set up the Label widget to create display box and placing text or images.

the_data= StringVar(value="") #initialize string variable with empty string
GUI_Label=Label(
    GUI_Window,
    text="Label",
    anchor=SE, #the widget will be located in the bottom right corner of the frame
    font=("Bell MT",20),
    textvariable=the_data, #we can retrive current text from entry widget.
    background="#FFE873",
    foreground="#646464"
    )
GUI_Label.pack(expand=True,fill="both")
#We have then used the pack() method with the Label's object and set the value of the expand parameter to True. The expand parameter is responsible for the expansion of the parent widget.
#Tkinter offers widget called FRAME. This helps us to group and arrange other widgets in one way or another friendly manner. Frames work like a container, those are accountable for organizing the position of the other widgets. This utilizes the rectangle area of the screen to organize the layout and offer padding of these widgets.
#variableName=Frame(parentWindow,options?)

FrameOne=Frame(GUI_Window,bg="#4B8BBE")#1st frame
FrameOne.pack(expand=True,fill="both")
    
FrameTwo=Frame(GUI_Window,bg="#306998")#2nd frame
FrameTwo.pack(expand=True,fill="both")    
    
FrameThree=Frame(GUI_Window,bg="#4B8BBE")#3rd frame
FrameThree.pack(expand=True,fill="both")

FrameFour=Frame(GUI_Window,bg="#306998")#4th frame
FrameFour.pack(expand=True,fill="both")
#We can create frame as per our preferences with suitable background color to beautify our frame.

#Now we will create the buttons for our calculator:

#1
ButtonOne=Button(
    FrameOne,
    text="1",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_1_is_clicked
    )
ButtonOne.pack(side=LEFT,expand=True,fill="both")

#2
ButtonTwo=Button(
    FrameOne,
    text="2",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_2_is_clicked
    )
ButtonTwo.pack(side=LEFT,expand=True,fill="both")

#3
ButtonThree=Button(
    FrameOne,
    text="3",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_3_is_clicked
    )
ButtonThree.pack(side=LEFT,expand=True,fill="both")

#Clear
ButtonClear=Button(
    FrameOne,
    text="Clr",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_clr_is_clicked
    )
ButtonClear.pack(side=LEFT,expand=True,fill="both")

#4
ButtonFour=Button(
    FrameTwo,
    text="4",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_4_is_clicked
    )
ButtonFour.pack(side=LEFT,expand=True,fill="both")

#5
ButtonFive=Button(
    FrameTwo,
    text="5",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_5_is_clicked
    )
ButtonFive.pack(side=LEFT,expand=True,fill="both")

#6
ButtonSix=Button(
    FrameTwo,
    text="6",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_6_is_clicked
    )
ButtonSix.pack(side=LEFT,expand=True,fill="both")

#addition
ButtonAdd=Button(
    FrameTwo,
    text="+",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_add_is_clicked
    )
ButtonAdd.pack(side=LEFT,expand=True,fill="both")

#7
ButtonSeven=Button(
    FrameThree,
    text="7",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_7_is_clicked
    )
ButtonSeven.pack(side=LEFT,expand=True,fill="both")

#8
ButtonEight=Button(
    FrameThree,
    text="8",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_8_is_clicked
    )
ButtonEight.pack(side=LEFT,expand=True,fill="both")

#9
ButtonNine=Button(
    FrameThree,
    text="9",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_9_is_clicked
    )
ButtonNine.pack(side=LEFT,expand=True,fill="both")

#Subtraction:
ButtonSub=Button(
    FrameThree,
    text="-",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_sub_is_clicked
    )
ButtonSub.pack(side=LEFT,expand=True,fill="both")

#Multiplication:
ButtonMul=Button(
    FrameFour,
    text="*",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_mul_is_clicked
    )
ButtonMul.pack(side=LEFT,expand=True,fill="both")

#0
ButtonZero=Button(
    FrameFour,
    text="0",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_0_is_clicked
    )
ButtonZero.pack(side=LEFT,expand=True,fill="both")

#Equal:
ButtonEqual=Button(
    FrameFour,
    text="=",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_equal_is_clicked
    )
ButtonEqual.pack(side=LEFT,expand=True,fill="both")

#Division:
ButtonDiv=Button(
    FrameFour,
    text="/",
    font=("Comic Sans MS",20),
    relief=GROOVE,
    border=1,
    command=button_div_is_clicked
    )
ButtonDiv.pack(side=LEFT,expand=True,fill="both")

GUI_Window.mainloop() #GUI running




