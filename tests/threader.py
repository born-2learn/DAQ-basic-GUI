import time
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import *
import serial
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

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


# DO
doPage = ttk.Frame(nb)
nb.add(doPage, text='Digital Output')


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

    while (1):
        try:
            serial_data = serial_object.readline()
            serial_data = serial_data.decode("utf-8")
            serial_data.rstrip('\r\n')
            # serial_data = serial_object.readline()

            filter_data = serial_data.split(',')

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

    text.place(x=15, y=10)
    progress_1.place(x=60, y=100)
    # l1.place(x=60, y=100)
    l1.pack()
    #progress_2.place(x=60, y=130)
    '''
    progress_3.place(x=60, y=160)
    progress_4.place(x=60, y=190)
    progress_5.place(x=60, y=220)
    progress_6.place(x=60, y=250)
    progress_7.place(x=60, y=280)
    progress_8.place(x=60, y=310)
    progress_9.place(x=60, y=340)
    progress_10.place(x=60, y=370)
    progress_11.place(x=60, y=400)
    progress_12.place(x=60, y=430)
    progress_13.place(x=60, y=460)
    progress_14.place(x=60, y=490)
    progress_15.place(x=60, y=520)
    progress_16.place(x=60, y=550)
    '''
    new = time.time()
    global var
    while (1):
        if filter_data:

            var = 0
            text.delete("1.0", END)
            try:
                filter_data[0] = float(filter_data[0])
            except:
                filter_data[0] = ''

            text.insert(END, filter_data[0])
            #text.insert(END, "\n")
            try:


                progress_1["value"] = filter_data[0]
                var = filter_data[0]
                #progress_2["value"] = filter_data[1]
                '''
                progress_3["value"] = filter_data[2]
                progress_4["value"] = filter_data[3]
                progress_5["value"] = filter_data[4]
                progress_6["value"] = filter_data[5]
                progress_7["value"] = filter_data[6]
                progress_8["value"] = filter_data[7]
                progress_9["value"] = filter_data[8]
                progress_10["value"] = filter_data[9]
                progress_11["value"] = filter_data[10]
                progress_12["value"] = filter_data[11]
                progress_13["value"] = filter_data[12]
                progress_14["value"] = filter_data[13]
                progress_15["value"] = filter_data[14]
                progress_16["value"] = filter_data[15]
                '''


            except:
                print('Error! Unable to store data as values to progress bars.')

            if time.time() - new >= update_period:
                text.delete("1.0", END)
                progress_1["value"] = 0
                '''
                progress_2["value"] = 0
                progress_3["value"] = 0
                progress_4["value"] = 0
                progress_5["value"] = 0
                progress_6["value"] = 0
                progress_7["value"] = 0
                progress_8["value"] = 0
                progress_9["value"] = 0
                progress_10["value"] = 0
                progress_11["value"] = 0
                progress_12["value"] = 0
                progress_13["value"] = 0
                progress_14["value"] = 0
                progress_15["value"] = 0
                progress_16["value"] = 0
                '''
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
    frame_1 = Frame(height=285, width=480, bd=3, relief='groove').place(x=7, y=5)
    frame_2 = Frame(height=150, width=480, bd=3, relief='groove').place(x=7, y=300)
    text = Text(width=30, height=1)

    # threads
    t2 = threading.Thread(target=update_main)
    t2.daemon = True
    t2.start()

    # Labels
    data1_ = Label(text="Thermocouple 1").place(x=15, y=100)
    '''
    data2_ = Label(text="Thermocouple 2").place(x=15, y=130)
    data3_ = Label(text="Thermocouple 3").place(x=15, y=160)
    data4_ = Label(text="Thermocouple 4").place(x=15, y=190)
    data5_ = Label(text="Thermocouple 5").place(x=15, y=220)
    data6_ = Label(text="Thermocouple 6").place(x=15, y=250)
    data7_ = Label(text="Thermocouple 7").place(x=15, y=280)
    data8_ = Label(text="Thermocouple 8").place(x=15, y=310)
    data9_ = Label(text="Data9:").place(x=15, y=340)
    data10_ = Label(text="Data10:").place(x=15, y=370)
    data11_ = Label(text="Data11:").place(x=15, y=400)
    data12_ = Label(text="Data12:").place(x=15, y=430)
    data13_ = Label(text="Data13:").place(x=15, y=460)
    data14_ = Label(text="Data14:").place(x=15, y=490)
    data15_ = Label(text="Data15:").place(x=15, y=520)
    data16_ = Label(text="Data16:").place(x=15, y=550)
    '''

    # progress_bars
    # Labels
    var = 10
    #print("FIlter data in _main_ -------------------------", filter_data)
    l1 = ttk.Label(text='he', textvariable=var)
    # label1.pack()
    progress_1 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    '''
    progress_2 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_3 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_4 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_5 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_6 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_7 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_8 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_9 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_10 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_11 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_12 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_13 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_14 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_15 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    progress_16 = ttk.Progressbar(orient=HORIZONTAL, mode='determinate', length=200, max=255)
    '''


    button_var = IntVar()



    connect = Button(text="Connect", command=connect).place(x=15, y=360)
    disconnect = Button(text="Disconnect", command=disconnect).place(x=300, y=360)

    # mainloop
    main.geometry('500x500')
    main.mainloop()
