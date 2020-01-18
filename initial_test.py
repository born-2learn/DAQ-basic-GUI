from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time


pinList=[25,17,18,27,22,23,24,10]

for i in pinList:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,GPIO.LOW)
    

main = Tk()
main.title('CITRIOT')
ttk.Label(main, text="Citriot Data Acquisition System").grid(row=0)

def toggledo1():

        if do1.config('text')[-1] == 'ON':
                do1.config(text='OFF')
                GPIO.output(25,GPIO.LOW)
        else:
                do1.config(text='ON')
                GPIO.output(25,GPIO.HIGH)

def toggledo2():
       
        if do2.config('text')[-1] == 'ON':
                do2.config(text='OFF')
                GPIO.output(17,GPIO.LOW)
        
        else:
                do2.config(text='ON')
                GPIO.output(17,GPIO.HIGH)

def toggledo3():

        if do3.config('text')[-1] == 'ON':
                do3.config(text='OFF')
                GPIO.output(18,GPIO.LOW)
        else:
                do3.config(text='ON')
                GPIO.output(18,GPIO.HIGH)

def toggledo4():

        if do4.config('text')[-1] == 'ON':
                do4.config(text='OFF')
                GPIO.output(27,GPIO.LOW)
                
        else:
                do4.config(text='ON')
                GPIO.output(27,GPIO.HIGH)

def toggledo5():

        if do5.config('text')[-1] == 'ON':
                do5.config(text='OFF')
                GPIO.output(22,GPIO.LOW)
        else:
                do5.config(text='ON')
                GPIO.output(22,GPIO.HIGH)

def toggledo6():

        if do6.config('text')[-1] == 'ON':
                do6.config(text='OFF')
                GPIO.output(23,GPIO.LOW)
        else:
                do6.config(text='ON')
                GPIO.output(23,GPIO.HIGH)

def toggledo7():

        if do7.config('text')[-1] == 'ON':
                do7.config(text='OFF')
                GPIO.output(24,GPIO.LOW)
        else:
                do7.config(text='ON')
                GPIO.output(24,GPIO.HIGH)

def toggledo8():

        if do8.config('text')[-1] == 'ON':
                do8.config(text='OFF')
                GPIO.output(10,GPIO.LOW)
        else:
                do8.config(text='ON')
                GPIO.output(10,GPIO.HIGH)

main.geometry('500x500')

# gives weight to the cells in the grid
rows = 0
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')


# About
aboutPage = ttk.Frame(nb)
nb.add(aboutPage, text='About')
#image = PhotoImage(file="logo.gif")
#L = Label(aboutPage, image=image).pack()

image = Image.open("logo.jpg")
image = image.resize((500, 250), Image.ANTIALIAS) ## The (250, 250) is (height, width)
img = ImageTk.PhotoImage(image)
panel = Label(aboutPage, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
Label(aboutPage, text = "Citriot Data Acquisition System",font=("Helvetica", 24) ).pack()




# DO
doPage = ttk.Frame(nb)
nb.add(doPage, text='Digital Output')

Label(doPage, text="DO 1").grid(column=0,row=1,padx=10,pady=10)
do1 = Button(doPage, text="OFF", width=12, command=toggledo1)
do1.grid(row=1, column = 1)

Label(doPage, text="DO 2").grid(column=0,row=2,padx=10,pady=10)
do2 = Button(doPage, text="OFF", width=12, command=toggledo2)
do2.grid(row=2, column = 1)

Label(doPage, text="DO 3").grid(column=0,row=3,padx=10,pady=10)
do3 = Button(doPage, text="OFF", width=12, command=toggledo3)
do3.grid(row=3, column = 1)

Label(doPage, text="DO 4").grid(column=0,row=4,padx=10,pady=10)
do4 = Button(doPage, text="OFF", width=12, command=toggledo4)
do4.grid(row=4, column = 1)

Label(doPage, text="DO 5").grid(column=0,row=5,padx=10,pady=10)
do5 = Button(doPage, text="OFF", width=12, command=toggledo5)
do5.grid(row=5, column = 1)

Label(doPage, text="DO 6").grid(column=0,row=6,padx=10,pady=10)
do6 = Button(doPage, text="OFF", width=12, command=toggledo6)
do6.grid(row=6, column = 1)

Label(doPage, text="DO 7").grid(column=0,row=7,padx=10,pady=10)
do7 = Button(doPage, text="OFF", width=12, command=toggledo7)
do7.grid(row=7, column = 1)

Label(doPage, text="DO 8").grid(column=0,row=8,padx=10,pady=10)
do8 = Button(doPage, text="OFF", width=12, command=toggledo8)
do8.grid(row=8, column = 1)









# DI

diPage = ttk.Frame(nb)
nb.add(diPage, text='Digital Input')








# Thermocouple
thermocouplePage = ttk.Frame(nb)
nb.add(thermocouplePage, text='Thermocouple')
#nb.Label(main, text="Citriot Data Acquisition System").grid(row=5)










# Analog Input
analogPage = ttk.Frame(nb)
nb.add(analogPage, text='Analog Input')








main.mainloop()