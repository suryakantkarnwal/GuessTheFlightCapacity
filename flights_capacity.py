class Flights():
    def __init__ (self,capacity):
        self.capacity=capacity
        self.passenger=[]
    def add_passenger(self,name):
        if not self.seats_remaining():
            return False
        self.passenger.append(name)
        return True


    def seats_remaining(self):
        return self.capacity-len(self.passenger) 

flight1= Flights(3)

people=["harry","ron","sam","pam","draco"]

for person in people:
    if flight1.add_passenger(person):
        print(f"{person} is added to the flight")
    else:
        print(f"{person} couldn't make to the flight because seats are full")    

print(flight1.passenger)