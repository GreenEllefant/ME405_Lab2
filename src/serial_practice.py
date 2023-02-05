import serial
from matplotlib import pyplot

def plotter():

    with serial.Serial('COM4', 115200) as serialPort:
        val_list = serialPort.readline().split(b',')

        get_axis = ('time in seconds', 'position in encoder ticks')              #isolate axis titles
        xpoints =[]
        ypoints =[]
        for i in range(len(val_list)-1):
            try:
                xpoints.append(float(val_list[i][0]))            #add only numerical values to plot list
                ypoints.append(float(val_list[i][1]))
            except ValueError:
                continue

        pyplot.plot(xpoints, ypoints)           
        pyplot.xlabel(get_axis[0])
        pyplot.ylabel(get_axis[1])
        pyplot.show()  