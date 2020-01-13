import serial

def temp_data():
    ser = serial.Serial('/dev/ttyUSB0',9600)
    
    values = []
    temp_list =[]
    while True:
        data = ser.readline()   #read data from serial
        
        if data:                #if there is data, append it to s
            
            values.append(data)
            
        print(len(values))
        if len(values) == 4:         #when s is 3 elements long, (all data has been retrieved)
            print('val',values)
            for temperature in values:
                try:
                    temperature = temperature.decode("utf-8")
                    if (temperature!='NaN'):
                        temperature = temperature.rstrip('\r\n')
                        temp_list.append(temperature)
                    else:
                        temp_list.append(0)
                except:
                    temp_list.append(0)
            print(temp_list)
            values = []
    return temp_list

while True:
    print(temp_data())