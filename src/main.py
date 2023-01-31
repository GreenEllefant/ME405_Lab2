'''!
main
'''

import utime
import position_control
import encoder_reader
import motor_driver

def main():
    # Set up encoder
    en1_pin = pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.IN)
    en2_pin = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.IN)
    timer4 = pyb.Timer(4, prescaler=0, period=0xFFFF)
    e = Encoder_Reader(en1_pin, en2_pin, timer4)
    
    # Set up motor
    en_pin = pyb.Pin(pyb.Pin.board.PA10, pby.Pin.OUT_OD, pyb.Pin.PULL_UP)
    in1pin = pyb.Pin(pyb.Pin.board.PB4, pby.Pin.OUT_PP)
    in2pin = pyb.Pin(pyb.Pin.board.PB5, pby.Pin.OUT_PP)
    timer3 = pyb.Timer(3, prescaler = 0, period = 0xFFFF)
    m = MotorDriver(en_pin, in1pin, in2pin, timer3)
    
    # Set up control class
    Kp = 1
    setpoint = 50
    c = Position_Control(Kp, setpoint, e, m)
    
    # main loop
    while True:
        
        
        
        utime.sleep_ms(10)
    
if __name__ == "__main__":
    main()
