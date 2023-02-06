"""! @encoder_class.py
This file contains code definitions for encoder behavior. 

@author Jack Ellsworth, Hannah Howe, Mathew Smith
@date   24-Jan-2023
@copyright (c) 2023 by Nobody and released under GNU Public License v3
"""
import time
import pyb
    
class Encoder_Reader:
    """!
    This class contains code for reading the encoder
    """
    def __init__(self, en1_pin, en2_pin, timer4):
        """!
        This class contains code for reading the encoder

        @param en1_pin: Encoder channel A pin
        @param en2_pint: Encoder channel B pin
        @param timer4: Timer channel for encoder
        """
        self.en1_pin = en1_pin
        self.en2_pin = en2_pin
        self.timer4 = timer4
        self.reference_count = self.timer4.counter()
        self.prev_pos = 0
        self.timer4.callback(self.handleflow)
        self.ch1B = self.timer4.channel(1, pyb.Timer.ENC_AB, pin=en1_pin)
        self.ch2B = self.timer4.channel(2, pyb.Timer.ENC_AB, pin=en2_pin)
        self.zero()

    def read(self):
        """!
        
        """
        self.prev_pos = self.timer4.counter() 
        return self.prev_pos - self.reference_count

    def zero(self):
        self.reference_count = self.timer4.counter()

    def handleflow(self, tim):
        current = self.timer4.counter()
        print("Hello World: ",current)
        if(current < self.prev_pos):
            self.reference_count -= 0xFFFF
        else:
            self.reference_count += 0xFFFF

if __name__ == "__main__":
    en1_pin = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN)
    en2_pin = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN)
    timer4 = pyb.Timer(4, prescaler=0, period=0xFFFF) 
    reader = Encoder_Reader(en1_pin, en2_pin, timer4)
    for i in range(0, 50):
        print(reader.read())
        time.sleep(0.1)

