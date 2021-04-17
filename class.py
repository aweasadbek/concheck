
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Capacity():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
        else:
            print(f"All {self.capacity} seats are full")
    def show_passengers_list(self):
        if self.passengers:
            for i in range(0, len(self.passengers)):
                print(f"{i+1} {self.passengers[i]}")
        else:
            print("Empty")

lambda a: a
NY074 = Capacity(5)
NY074.show_passengers_list()
NY074.add_passenger("Mobile apps")
NY074.add_passenger("Web Apps")
NY074.add_passenger("Physics")
NY074.add_passenger("Robotics")
NY074.add_passenger("Fundamentals")
NY074.add_passenger("Design")
NY074.show_passengers_list()
