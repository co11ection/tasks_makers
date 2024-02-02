class Auto:

    def ride(self) -> None:
        print("Riding on a ground")


class Boat:

    def swim(self) -> None:
        print("Floating on water") 


class Amphibian(Auto, Boat):
    pass


obj = Amphibian() 

obj.ride() 
obj.swim()
