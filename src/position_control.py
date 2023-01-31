import utime

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

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint
    
    def set_Kp(self, gain):
        self.gain = gain

    def print_values(self):
        for i in range(0, len(self.values[0])):
            print(str(self.values[0][i]) + "," + str(self.values[1][i]))