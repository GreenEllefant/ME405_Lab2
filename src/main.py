'''!
main
'''

import utime
#import position_control
import encoder_reader
from motor_driver import Motor_Driver

#------------ Position control Code

class Position_Control:
    
    def __init__(self, gain, setpoint, encoder, motor):
        self.gain = gain
        self.setpoint = setpoint
        self.values = [[], []]
        self.encoder = encoder
        self.motor = motor
        self.time = utime.ticks_ms()

    def run(self, setpoint):
        self.setpoint = setpoint
        self.values[0].append(utime.ticks_ms() - self.time)
        self.values[1].append(self.encoder.read())
        self.motor.set_duty_cycle(self.gain * (self.setpoint - self.encoder.read()))

    def reset_values(self):
        self.values = [[], []]
        self.time = utime.ticks_ms()

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint
    
    def set_Kp(self, gain):
        self.gain = gain

    def print_values(self):
        for i in range(0, len(self.values[0])):
            print(str(self.values[0][i]) + "," + str(self.values[1][i]))

#----------------------------------------------

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
    c = Position_Control(Kp, setpoints[0], e, m)
    
    # main loop
    # Move to each set point for 3 seconds
    for i in setpoints:
        stop = utime.ticks_ms()+3000
        while utime.ticks_ms() < stop:
            c.run(i)
            utime.sleep_ms(10)
        e.zero()
        c.print_values()
        c.reset_values()
    m.set_duty_cycle(0)
    print("END OF PROGRAM")
    
if __name__ == "__main__":
    main()
