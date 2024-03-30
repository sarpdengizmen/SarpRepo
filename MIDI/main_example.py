
import time
import builtins
import uselect
import sys
from machine import Pin, PWM, Timer

class Stepper:
    def __init__(self, direction_pin, step_pin, freq=500):
        self.direction_pin = Pin(direction_pin, Pin.OUT)
        self.step_pin = PWM(Pin(step_pin))
        self.steps = 0
        self.timer = Timer()

    def set_direction(self, direction):
        self.direction_pin.value(direction)


    def start(self, freq=500, duty=32768):
        self.step_pin.freq(freq)
        self.step_pin.duty_u16(duty)
        self.timer.init(mode=Timer.PERIODIC, freq=self.step_pin.freq(), callback=self._step)

    def stop(self):
        self.step_pin.duty_u16(0)
        self.steps = 0
        self.timer.deinit()

    def _step(self, timer):
        self.steps += 1



class SerialComm:
    def __init__(self):
        self.serialPoll = uselect.poll()
        self.serialPoll.register(sys.stdin, uselect.POLLIN)
        pass

    def read_message(self):
        return(sys.stdin.read(1) if self.serialPoll.poll(0) else None)

    def send_message(self, message):
        print(message)
    
    def read_parse(self):
        message = self.read_message()
        if message:
            return message.split(' ') 
        else:
            return None

def main():
    print('Hello World!')

    ser = SerialComm()
    while True:
        msg = ser.read_parse()
        if msg:
            print(msg + ['Hello'])

        
    
if __name__ == '__main__':
    main()