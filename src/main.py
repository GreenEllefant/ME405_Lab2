'''! @main.py
    This file sets up the motor, encoder, and a position controller. The program accepts a
    control parameter 'Kp' and then runs the motor for one rotation. The position is recorded
    every 10ms and once the run is complete the run data is sent via serial port. The data
    sent is the number of data points, the Kp value, and the time and position separated by
    a comma. The file 'Serial_plotter.py' receives and plots this data. 
    
    @author Jack Ellsworth, Hannah Howe, Mathew Smith
    @date   05-Feb-2023
    @copyright (c) 2023 by Nobody and released under GNU Public License v3
'''

import utime
import encoder_reader
from position_control import Position_Control
from motor_driver import Motor_Driver
from pyb import UART
pyb.repl_uart(None)

def main():
    # Set up encoder
    en1_pin = pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.IN)
    en2_pin = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.IN)
    timer3 = pyb.Timer(3, prescaler=0, period=0xFFFF)
    e = encoder_reader.Encoder_Reader(en1_pin, en2_pin, timer3)
    
    # Set up motor
    en_pin = pyb.Pin(pyb.Pin.board.PC1, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
    in1pin = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    in2pin = pyb.Pin(pyb.Pin.board.PA1, pyb.Pin.OUT_PP)
    timer5 = pyb.Timer(5, prescaler = 0, period = 0xFFFF)
    m = Motor_Driver(en_pin, in1pin, in2pin, timer5)
    
    
    # Set up control class
    Kp = 0.05
    # Move to these positions
    setpoints = [4000, 8000, 12000, 16000]
    c = Position_Control(Kp, 0, e, m)
    
    # Set up serial stuff
    u2 = pyb.UART(2, baudrate=115200)      # Set up the second USB-serial port
    
    # main loop
    # Run tests for 3s each
    while True:
        Kp = float(input("\n  Kp: "))
        c.set_Kp(Kp)
        c.reset_values()
        stop = utime.ticks_ms()+3000
        while utime.ticks_ms() < stop:
            c.run(4000)
            utime.sleep_ms(10)
        m.set_duty_cycle(0)
        e.zero()
        c.print_values()
        print(len(c.values[1]))
        u2.write(f"{len(c.values[1])}\r\n")
        u2.write(f"{Kp}\r\n")
        for i in range(0, len(c.values[0])):
            u2.write(f"{c.values[0][i]},{c.values[1][i]}\r\n")
    print("END OF PROGRAM")

if __name__ == "__main__":
    main()
