# This File Contains the Parent Class- Vehicle

class Vehicle:
    """Common Functionality for Every Vehicle in the Organization"""
    def __init__(self, number_plate:str, max_speed: int):
        self.number_plate=number_plate
        self.max_speed=max_speed
        self.current_speed=100
        self.engine_on=False

    def start_engine(self):
        if not self.engine_on:
            self.engine_on=True
            print(f"[{self.number_plate}] Engine Started")
        else:
            print(f"[{self.number_plate}] Engine is already Running")

    def stop_engine(self):
        if not self.engine_on:
            self.engine_on=False
            print(f"[{self.number_plate}] Engine Stopped")
        else:
            print(f"[{self.number_plate}] Engine is already Off")

    def accelarate(self,delta:int):
        if not self.engine_on:
            print(f"[{self.number_plate}] Start the Engine First")
        else:
            self.current_speed=min(self.max_speed,self.current_speed+delta)
            print(f"[{self.number_plate}] Accelarated. Current Speed: {self.current_speed}")

    def brake(self):
        self.current_speed=0
        print(f"[{self.number_plate}] Vehicle Fully Stopped")

    def status(self):
        p= {
            "plate":self.number_plate,
            "speed":self.current_speed,
            "max_speed":self.max_speed,
            "engine_on":self.engine_on
        }

        return print(p)



#v1=Vehicle("A1001",50)
# v1.engine_on=True
# v1.start_engine()
# v1.current_speed=10
# v1.accelarate(50)
# v1.status()



