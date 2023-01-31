class PropotionalControl:
    
    def __init__(self, gain, setpoint):
        self.gain = gain
        self.setpoint = setpoint


    def run(self, measured):
        return self.gain * (self.setpoint - measured)

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint
    
    def set_Kp(self, gain):
        self.gain = gain