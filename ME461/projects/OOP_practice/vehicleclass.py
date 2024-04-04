class Vehicle():
    def __init__(self, max_speed = 0, mileage = 0):
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f"Vehicle with max speed of {self.max_speed} and mileage of {self.mileage}"
    
    @property
    def max_speed(self):
        return self.__max_speed
    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError("Max speed cannot be negative")
        else:
            self.__max_speed = max_speed

class Bus(Vehicle):
    def __str__(self):
        return f"Bus with max speed of {self.max_speed} and mileage of {self.mileage}"

bus = Bus(180, 12)
print(bus)
