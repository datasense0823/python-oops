from vehicle import Vehicle

class Motorcycle(Vehicle):

    def __init__(self, number_plate:str, max_speed: int,color:str):

        super().__init__(number_plate,max_speed)
        self.helmet_on=False
        self.side_stand_down=True
        self.color=color


    def put_on_helmet(self):
        self.helmet_on=True
        print(f"[{self.number_plate}] Helmet On")

    def take_off_helmet(self):
        self.helmet_on=False
        print(f"[{self.number_plate}] Helmet Off")
        
    def status(self):
        data=super().status()
        data["helmet"]=self.helmet_on
        return print(data)



    

  

m1=Motorcycle("A001",100,"green")
# m1.engine_on=False
# m1.number_plate="A001"
m1.start_engine()
m1.status()






