from tkinter import *
#from ttkinter import ttk
from tkinter import ttk
import tkinter as tk

main = Tk()
main.title('CITRIOT')
ttk.Label(main, text="Citriot Data Acquisition System").grid(row=0)

def toggledo1():

        if do1.config('text')[-1] == 'ON':
                do1.config(text='OFF')
        else:
                do1.config(text='ON')

def toggledo2():
       
        if do2.config('text')[-1] == 'ON':
                do2.config(text='OFF')
        else:
                do2.config(text='ON')

def toggledo3():

        if do3.config('text')[-1] == 'ON':
                do3.config(text='OFF')
        else:
                do3.config(text='ON')

def toggledo4():

        if do4.config('text')[-1] == 'ON':
                do4.config(text='OFF')
        else:
                do4.config(text='ON')

def toggledo5():

        if do5.config('text')[-1] == 'ON':
                do5.config(text='OFF')
        else:
                do5.config(text='ON')

def toggledo6():

        if do6.config('text')[-1] == 'ON':
                do6.config(text='OFF')
        else:
                do6.config(text='ON')

def toggledo7():

        if do7.config('text')[-1] == 'ON':
                do7.config(text='OFF')
        else:
                do7.config(text='ON')

def toggledo8():

        if do8.config('text')[-1] == 'ON':
                do8.config(text='OFF')
        else:
                do8.config(text='ON')

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