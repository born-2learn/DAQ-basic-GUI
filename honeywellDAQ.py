#!/usr/bin/python3

import time
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import *
import serial
from PIL import Image, ImageTk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

doPinlist = [25, 17, 18, 27, 22, 23, 24, 10]
diPinlist = [5, 6, 13, 19, 26, 16, 20, 21]

for i in doPinlist:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

for i in diPinlist:
    GPIO.setup(i, GPIO.IN)


serial_data = ''
filter_data = ''
update_period = 5
serial_object = None
main = Tk()
main.title("Citriot DAQ")


def toggledo1():
    if do1.config('text')[-1] == 'ON':
        do1.config(text='OFF')
        GPIO.output(25, GPIO.LOW)
    else:
        do1.config(text='ON')
        GPIO.output(25, GPIO.HIGH)


def toggledo2():
    if do2.config('text')[-1] == 'ON':
        do2.config(text='OFF')
        GPIO.output(17, GPIO.LOW)

    else:
        do2.config(text='ON')
        GPIO.output(17, GPIO.HIGH)


def toggledo3():
    if do3.config('text')[-1] == 'ON':
        do3.config(text='OFF')
        GPIO.output(18, GPIO.LOW)
    else:
        do3.config(text='ON')
        GPIO.output(18, GPIO.HIGH)


def toggledo4():
    if do4.config('text')[-1] == 'ON':
        do4.config(text='OFF')
        GPIO.output(27, GPIO.LOW)

    else:
        do4.config(text='ON')
        GPIO.output(27, GPIO.HIGH)


def toggledo5():
    if do5.config('text')[-1] == 'ON':
        do5.config(text='OFF')
        GPIO.output(22, GPIO.LOW)
    else:
        do5.config(text='ON')
        GPIO.output(22, GPIO.HIGH)


def toggledo6():
    if do6.config('text')[-1] == 'ON':
        do6.config(text='OFF')
        GPIO.output(23, GPIO.LOW)
    else:
        do6.config(text='ON')
        GPIO.output(23, GPIO.HIGH)


def toggledo7():
    if do7.config('text')[-1] == 'ON':
        do7.config(text='OFF')
        GPIO.output(24, GPIO.LOW)
    else:
        do7.config(text='ON')
        GPIO.output(24, GPIO.HIGH)


def toggledo8():
    if do8.config('text')[-1] == 'ON':
        do8.config(text='OFF')
        GPIO.output(10, GPIO.LOW)
    else:
        do8.config(text='ON')
        GPIO.output(10, GPIO.HIGH)


# gives weight to the cells in the grid
rows = 0
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1


def connect():
    """The function initiates the Connection to the UART device with the Port and Buad fed through the Entry
    boxes in the application.
    The radio button selects the platform, as the serial object has different key phrases
    for Linux and Windows. Some Exceptions have been made to prevent the app from crashing,
    such as blank entry fields and value errors, this is due to the state-less-ness of the
    UART device, the device sends data at regular intervals irrespective of the master's state.
    The other Parts are self explanatory.
    """

    version_ = button_var.get()

    global serial_object

    baud = 9600
    try:
        serial_object = serial.Serial('/dev/ttyACM0', baud)

    except:
        print("Can't open port ACM0")

    t1 = threading.Thread(target=get_data)
    t1.daemon = True
    t1.start()


def get_data():
    """This function serves the purpose of collecting data from the serial object and storing
    the filtered data into a global variable.
    The function has been put into a thread since the serial event is a blocking function.
    """
    global serial_object
    global filter_data
    global di_data
    di_data = [0,0,0,0,0,0,0,0]
    while (1):
        try:
            serial_data = serial_object.readline()
            serial_data = serial_data.decode("utf-8")
            serial_data.rstrip('\r\n')
            # serial_data = serial_object.readline()

            filter_data = serial_data.split(',')
            for i in range(len(filter_data)):
                if float(filter_data[i])>500.00 or float(filter_data[i])==0:
                    filter_data[i] = 'NAN'


            for i in range(len(diPinlist)):
                di_data[i] = GPIO.input(diPinlist[i])
                if di_data[i]==1:
                    di_data[i] = 'OFF'
                else:
                    di_data[i] = 'ON'


            print(filter_data)

        except TypeError:
            pass


def update_main():
    """" This function is an update function which is also threaded. The function assimilates the data
    and applies it to it corresponding progress bar. The text box is also updated every couple of seconds.
    A simple auto refresh function .after() could have been used, this has been avoid purposely due to
    various performance issues.
    """
    global filter_data
    global update_period
    global di_data

    # thermocouple component packing(label: text)
    thermocoupleText1.grid(column=2, row=1)
    thermocoupleText2.grid(column=2, row=2)
    thermocoupleText3.grid(column=2, row=3)
    thermocoupleText4.grid(column=2, row=4)
    thermocoupleText5.grid(column=2, row=5)
    thermocoupleText6.grid(column=2, row=6)
    thermocoupleText7.grid(column=2, row=7)
    thermocoupleText8.grid(column=2, row=8)

    analogText1.grid(column = 2, row=1)
    analogText2.grid(column=2, row=2)
    analogText3.grid(column=2, row=3)
    analogText4.grid(column=2, row=4)
    analogText5.grid(column=2, row=5)
    analogText6.grid(column=2, row=6)
    analogText7.grid(column=2, row=7)
    analogText8.grid(column=2, row=8)

    diText1.grid(column=2, row=1)
    diText2.grid(column=2, row=2)
    diText3.grid(column=2, row=3)
    diText4.grid(column=2, row=4)
    diText5.grid(column=2, row=5)
    diText6.grid(column=2, row=6)
    diText7.grid(column=2, row=7)
    diText8.grid(column=2, row=8)






    new = time.time()
    global var
    while (1):
        if filter_data:

            var = 0
            var = filter_data[0]



            thermocoupleText1.config(text = filter_data[0])
            thermocoupleText2.config(text = filter_data[1])
            thermocoupleText3.config(text = filter_data[2])
            thermocoupleText4.config(text = filter_data[3])
            thermocoupleText5.config(text = filter_data[4])
            thermocoupleText6.config(text = filter_data[5])
            thermocoupleText7.config(text = filter_data[6])
            thermocoupleText8.config(text = filter_data[7])

            analogText1.config(text = filter_data[8])
            analogText2.config(text = filter_data[9])
            analogText3.config(text = filter_data[10])
            analogText4.config(text = filter_data[11])
            analogText5.config(text = filter_data[12])
            analogText6.config(text = filter_data[13])
            analogText7.config(text = filter_data[14])
            analogText8.config(text = filter_data[15])

            diText1.config(text = di_data[0])
            diText2.config(text=di_data[1])
            diText3.config(text=di_data[2])
            diText4.config(text=di_data[3])
            diText5.config(text=di_data[4])
            diText6.config(text=di_data[5])
            diText7.config(text=di_data[6])
            diText8.config(text=di_data[7])


            if time.time() - new >= update_period:
                new = time.time()


def disconnect():
    """
    This function is for disconnecting and quitting the application.
    Sometimes the application throws a couple of errors while it is being shut down, the fix isn't out yet
    but will be pushed to the repo once done.
    simple main.quit() calls.
    """
    try:
        serial_object.close()

    except AttributeError:
        print("Closed without Using it -_-")

    main.quit()


if __name__ == "__main__":
    """
    The main loop consists of all the main objects and its placement.
    The Main loop handles all the widget placements.
    """
    global var
    # frames
    # frame_1 = Frame(height=285, width=480, bd=3, relief='groove').place(x=7, y=5)
    # frame_2 = Frame(height=150, width=480, bd=3, relief='groove').place(x=7, y=300)
    nb = ttk.Notebook(main)
    nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

    # About
    aboutPage = ttk.Frame(nb)
    nb.add(aboutPage, text='About')
    # image = PhotoImage(file="logo.gif")
    # L = Label(aboutPage, image=image).pack()

    image = Image.open("logo.jpg")
    image = image.resize((500, 250), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
    img = ImageTk.PhotoImage(image)
    panel = Label(aboutPage, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    Label(aboutPage, text="Citriot Data Acquisition System", font=("Helvetica", 24)).pack()

    doPage = ttk.Frame(nb)
    nb.add(doPage, text='Digital Output')

    Label(doPage, text="DO 1").grid(column=0, row=1, padx=10, pady=10)
    do1 = Button(doPage, text="OFF", width=12, command=toggledo1)
    do1.grid(row=1, column=1)

    Label(doPage, text="DO 2").grid(column=0, row=2, padx=10, pady=10)
    do2 = Button(doPage, text="OFF", width=12, command=toggledo2)
    do2.grid(row=2, column=1)

    Label(doPage, text="DO 3").grid(column=0, row=3, padx=10, pady=10)
    do3 = Button(doPage, text="OFF", width=12, command=toggledo3)
    do3.grid(row=3, column=1)

    Label(doPage, text="DO 4").grid(column=0, row=4, padx=10, pady=10)
    do4 = Button(doPage, text="OFF", width=12, command=toggledo4)
    do4.grid(row=4, column=1)

    Label(doPage, text="DO 5").grid(column=0, row=5, padx=10, pady=10)
    do5 = Button(doPage, text="OFF", width=12, command=toggledo5)
    do5.grid(row=5, column=1)

    Label(doPage, text="DO 6").grid(column=0, row=6, padx=10, pady=10)
    do6 = Button(doPage, text="OFF", width=12, command=toggledo6)
    do6.grid(row=6, column=1)

    Label(doPage, text="DO 7").grid(column=0, row=7, padx=10, pady=10)
    do7 = Button(doPage, text="OFF", width=12, command=toggledo7)
    do7.grid(row=7, column=1)

    Label(doPage, text="DO 8").grid(column=0, row=8, padx=10, pady=10)
    do8 = Button(doPage, text="OFF", width=12, command=toggledo8)
    do8.grid(row=8, column=1)

    # DI

    diPage = ttk.Frame(nb)
    nb.add(diPage, text='Digital Input')

    diText1 = Label(diPage, text='OFF', font=("Courier", 15))
    diText2 = Label(diPage, text='OFF', font=("Courier", 15))
    diText3 = Label(diPage, text='OFF', font=("Courier", 15))
    diText4 = Label(diPage, text='OFF', font=("Courier", 15))
    diText5 = Label(diPage, text='OFF', font=("Courier", 15))
    diText6 = Label(diPage, text='OFF', font=("Courier", 15))
    diText7 = Label(diPage, text='OFF', font=("Courier", 15))
    diText8 = Label(diPage, text='OFF', font=("Courier", 15))




    # Thermocouple
    thermocouplePage = ttk.Frame(nb)
    nb.add(thermocouplePage, text='Thermocouple')
    # nb.Label(main, text="Citriot Data Acquisition System").grid(row=5)

    thermocoupleText1 = Label(thermocouplePage, text='Loading...', font=("Courier", 15))
    thermocoupleText2 = Label(thermocouplePage, text='Loading...', font=("Courier", 15))
    thermocoupleText3 = Label(thermocouplePage, text='Loading...', font=("Courier", 15))
    thermocoupleText4 =Label(thermocouplePage, text='Loading...', font=("Courier", 15))
    thermocoupleText5 = Label(thermocouplePage, text='Loading...', font=("Courier", 15))
    thermocoupleText6 = Label(thermocouplePage, text='Loading...', font=("Courier", 15))
    thermocoupleText7 = Label(thermocouplePage, text='Loading...', font=("Courier", 15))
    thermocoupleText8 = Label(thermocouplePage, text='Loading...', font=("Courier", 15))



    # Analog Input
    analogPage = ttk.Frame(nb)
    nb.add(analogPage, text='Analog Input')

    analogText1 = Label(analogPage, text='Loading...', font=("Courier", 20))
    analogText2 = Label(analogPage, text='Loading...', font=("Courier", 20))
    analogText3 = Label(analogPage, text='Loading...', font=("Courier", 20))
    analogText4 = Label(analogPage, text='Loading...', font=("Courier", 20))
    analogText5 = Label(analogPage, text='Loading...', font=("Courier", 20))
    analogText6 = Label(analogPage, text='Loading...', font=("Courier", 20))
    analogText7 = Label(analogPage, text='Loading...', font=("Courier", 20))
    analogText8 = Label(analogPage, text='Loading...', font=("Courier", 20))

    accelerometerPage = ttk.Frame(nb)
    nb.add(accelerometerPage, text = 'Accelerometer')

    accText1x = Label(accelerometerPage, text='Loading...', font=("Courier", 20))
    accText2x = Label(accelerometerPage, text='Loading...', font=("Courier", 20))
    accText1y = Label(accelerometerPage, text='Loading...', font=("Courier", 20))
    accText2y = Label(accelerometerPage, text='Loading...', font=("Courier", 20))
    accText1z = Label(accelerometerPage, text='Loading...', font=("Courier", 20))
    accText2z = Label(accelerometerPage, text='Loading...', font=("Courier", 20))



    # threads
    t2 = threading.Thread(target=update_main)
    t2.daemon = True
    t2.start()

    # Labels
    thermocoupleLabel1 = Label(thermocouplePage, text="Thermocouple 1: ", font=("Courier", 15)).grid(column=1, row=1)
    thermocoupleLabel2 = Label(thermocouplePage, text="Thermocouple 2: ", font=("Courier", 15)).grid(column=1, row=2)
    thermocoupleLabel3 = Label(thermocouplePage, text="Thermocouple 3: ", font=("Courier", 15)).grid(column=1, row=3)
    thermocoupleLabel4 = Label(thermocouplePage, text="Thermocouple 4: ", font=("Courier", 15)).grid(column=1, row=4)
    thermocoupleLabel5 = Label(thermocouplePage, text="Thermocouple 5: ", font=("Courier", 15)).grid(column=1, row=5)
    thermocoupleLabel6 = Label(thermocouplePage, text="Thermocouple 6: ", font=("Courier", 15)).grid(column=1, row=6)
    thermocoupleLabel7 = Label(thermocouplePage, text="Thermocouple 7: ", font=("Courier", 15)).grid(column=1, row=7)
    thermocoupleLabel8 = Label(thermocouplePage, text="Thermocouple 8: ", font=("Courier", 15)).grid(column=1, row=8)

    analogLabel1 = Label(analogPage, text="Analog Input 1").grid(column=1, row=1)
    analogLabel2 = Label(analogPage, text="Analog Input 2").grid(column=1, row=2)
    analogLabel3 = Label(analogPage, text="Analog Input 3").grid(column=1, row=3)
    analogLabel4 = Label(analogPage, text="Analog Input 4").grid(column=1, row=4)
    analogLabel5 = Label(analogPage, text="Analog Input 5").grid(column=1, row=5)
    analogLabel6 = Label(analogPage, text="Analog Input 6").grid(column=1, row=6)
    analogLabel7 = Label(analogPage, text="Analog Input 7").grid(column=1, row=7)
    analogLabel8 = Label(analogPage, text="Analog Input 8").grid(column=1, row=8)

    diLabel1 = Label(diPage, text = "Digital Input 1: ").grid(column=1, row=1)
    diLabel2 = Label(diPage, text="Digital Input 2: ").grid(column=1, row=2)
    diLabel3 = Label(diPage, text="Digital Input 3: ").grid(column=1, row=3)
    diLabel4 = Label(diPage, text="Digital Input 4: ").grid(column=1, row=4)
    diLabel5 = Label(diPage, text="Digital Input 5: ").grid(column=1, row=5)
    diLabel6 = Label(diPage, text="Digital Input 6: ").grid(column=1, row=6)
    diLabel7 = Label(diPage, text="Digital Input 7: ").grid(column=1, row=7)
    diLabel8 = Label(diPage, text="Digital Input 8: ").grid(column=1, row=8)

    acc1x = Label(accelerometerPage, text='Accelerometer1 X Axis').grid(column = 1, row = 1)
    acc1y = Label(accelerometerPage, text='Accelerometer1 Y Axis').grid(column=1, row=2)
    acc1z = Label(accelerometerPage, text='Accelerometer1 Z Axis').grid(column=1, row=3)
    acc2x = Label(accelerometerPage, text='Accelerometer2 X Axis').grid(column=1, row=4)
    acc2y = Label(accelerometerPage, text='Accelerometer2 Y Axis').grid(column=1, row=5)
    acc2z = Label(accelerometerPage, text='Accelerometer2 Z Axis').grid(column=1, row=6)


    # progress_bars
    # Labels
    var = 10
    # print("FIlter data in _main_ -------------------------", filter_data)
    l1 = ttk.Label(text='he', textvariable=var)
    # label1.pack()

    progress_1 = ttk.Progressbar(thermocouplePage, orient=HORIZONTAL, mode='determinate', length=200, max=255)

    button_var = IntVar()

    connect = Button(text="Connect", command=connect).place(x=15, y=360)
    disconnect = Button(text="Disconnect", command=disconnect).place(x=300, y=360)

    # Defines and places the notebook widget

    # mainloop
    main.geometry('500x500')
    main.mainloop()
