# Create A Child Class Car Which Inherits from Parent Class Vehicle and add functionalities

from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,number_plate:str,max_speed:int,fuel_capacity:int =50,ac_on:bool=False):

        #Variables inherited from Parent Class
        super()._init__(number_plate,max_speed)_

        #Variables Defined in Child Class
        self.ac_on=ac_on
        self.fuel_capacity=fuel_capacity
        self.fuel_level=fuel_capacity
        self.cabin_temp=22

    def toggle_ac(self):
        self.ac_on=not self.ac_on
        state="ON" if self.ac_on else "OFF"
        print(f"[{self.number_plate}] AC {state}")

    def set_cabin_temperature(self,degrees:int):
        if not self.ac_on:
             print(f"[{self.number_plate}] AC is off. Temperature Unchanged")
        else:
            self.cabin_temp=degrees
            print(f"[{self.number_plate}] Cabin Set to {self.cabin_temp}")
    
    def refuel(self,litres:int):
        if litres<=0:
            print("Must be a Positive Value")
        else:
            new_level=min(self.fuel_capacity,self.fuel_level+litres)
            added=new_level-self.fuel_level
            self.fuel_level=new_level
            print(f"[{self.number_plate}] Added {added}  ")

    def status(self):
        data=super().status()
        data.update(
            {
                "ac":self.ac_on,
                "cabin_temp":self.cabin_temp,
                "fuel":f"{self.fuel_level}/{self.fuel_capacity}"
            }
        )





c1=Car("C001",100)
print(c1.fuel_capacity)



