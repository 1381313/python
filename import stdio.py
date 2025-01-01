
import random

class Car:
    

    def __init__(self, color, acc, brake, max_speed, fuel_cap, fuel_present, distance, fuel_consumption):
        
        self.color = color
        self.acc = acc
        self.brake = brake
        self.max_speed = max_speed
        self.fuel_cap = fuel_cap
        self.fuel_present = fuel_present
        self.distance = distance
        self.fuel_consumption = fuel_consumption

    def set_color(self):
        
        self.color = random.choice(["red", "blue", "green"])
        print("Your car is " + self.color)

    def accelerate(self, number):
       
        if number == 1:
            x = 10
        elif number == 2:
            x = 15
        elif number == 3:
            x = 12
        self.acc += x
        print(f"Your car speed is {self.acc}")

    def apply_brake(self, number):
        if number == 1:
            y = 15
        elif number == 2:
            y = 5
        elif number == 3:
            y = 12
        self.brake = y
        print(f"Your car brake is {self.brake} m/s")

    def set_max_speed(self):
        self.max_speed = 220
        print(f"Your car max speed is {self.max_speed}")

    def set_fuel_cap(self, number):
        if number == 1:
            z = 70
        elif number == 2:
            z = 50
        self.fuel_cap = z
        print(f"Your car fuel capacity is {self.fuel_cap}")
        self.fuel_present = self.fuel_cap - self.fuel_consumption
        print(f"Your car fuel present is {self.fuel_present}")

    def set_fuel_consumption(self, number):
        if number == 1:
            z = 9
        elif number == 2:
            z = 7
        elif number == 3:
            z = 6
        self.fuel_consumption = z
        print(f"Your car fuel consumption is {self.fuel_consumption}")