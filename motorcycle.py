from vehicle import Vehicle

class Motorcycle(Vehicle):

    def __init__(self, number_plate:str, max_speed: int,color:str):
        self.helmet_on=False
        self.side_stand_down=True
        self.color=color

    

  

m1=Motorcycle("A001",100,"green")
# m1.engine_on=False
# m1.number_plate="A001"
m1.start_engine()
m1.shout()





