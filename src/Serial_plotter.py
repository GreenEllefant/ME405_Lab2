"""! @Serial_plotter.py
    This file waits for the board to send data through the computer's COM5 serial port.
    @author Jack Ellsworth, Hannah Howe, Mathew Smith
    @date   30-Jan-2023
    @copyright (c) 2023 by Nobody and released under GNU Public License v3
"""

import serial
from matplotlib import pyplot

def plotter():
    val_list = []
    with serial.Serial('COM5', 115200) as serialPort:
        print(serialPort.name)
        thing = serialPort.readline().split(b',')
        kp = serialPort.readline().split(b',')
        #print(thing[0])
        for i in range(int(thing[0])):
            item = serialPort.readline().split(b',')
            val_list.append(item)
            

        get_axis = ('Time (in seconds)', 'Position (in encoder ticks)')              #isolate axis titles
        xpoints =[]
        ypoints =[]
        for i in range(len(val_list)-1):
            try:
                xpoints.append(float(val_list[i][0]))            #add only numerical values to plot list
                ypoints.append(float(val_list[i][1]))
            except ValueError:
                continue

        pyplot.plot(xpoints, ypoints)           
        pyplot.title("Impulse Response for Flywheel at given Gain (Kp: " + str(float(kp[0])) + ")" )
        pyplot.xlabel(get_axis[0])
        pyplot.ylabel(get_axis[1])
        pyplot.show()

def main():
    plotter()
    
if name == "__main__":
    main()