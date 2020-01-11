from tkinter import *
#from ttkinter import ttk
from tkinter import ttk
import tkinter as tk

main = Tk()
main.title('Notebook Demo 1 updated')
ttk.Label(main, text="Citriot Data Acquisition System").grid(row=0)

def toggledo1():

    if do1.config('text')[-1] == 'ON':
        do1.config(text='OFF')
    else:
        do1.config(text='ON')

def toggledo2():
        '''
        use
        t_btn.config('text')[-1]
        to get the present state of the toggle button
        '''
        if do2.config('text')[-1] == 'ON':
            do2.config(text='OFF')
        else:
            do2.config(text='ON')




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

Label(doPage, text="DO 1").grid(column=0,row=0,padx=10,pady=10)
do1 = Button(doPage, text="OFF", width=12, command=toggledo1)
do1.grid(row=0, column = 1)

Label(doPage, text="DO 2").grid(column=0,row=2,padx=10,pady=10)
do2 = Button(doPage, text="OFF", width=12, command=toggledo2)
do2.grid(row=2, column = 1)










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