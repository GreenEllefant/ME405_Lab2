"""! @Serial_plotter.py
    This file waits for the board to send data through the computer's COM5 serial port.
    Utilizes the Python PC compiler
    @author Jack Ellsworth, Hannah Howe, Mathew Smith
    @date   5-Feb-2023
    @copyright (c) 2023 by Nobody and released under GNU Public License v3
"""

import serial
from matplotlib import pyplot

"""!
@details: 
uses serial port to take in position and time data as 2D byte array
will return a plot of the points, number of points determined by response sent via UART
first two values read are length of data set and chosen gain respectively
"""

def plotter():
    val_list = []                                       
    with serial.Serial('COM5', 115200) as serialPort:
        print(serialPort.name)
        thing = serialPort.readline().split(b',')
        kp = serialPort.readline().split(b',')
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
    
if __name__ == "__main__":
    main()