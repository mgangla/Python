class Car :
    def __init__(self,make,model,year):        
        self.make = make
        self.model= model 
        self.year = year

    def start(self):
        return "Vroom"
    
    def stop (self) :
        return "screeth"

myCar = Car("Mercedes", "E Class", "2020")

print (myCar) 

class ElectricCar (Car):
    def __init__(self,make,model,year):
        Car.__init__(self,make,model,year)

myElectricCar = ElectricCar("Subaru", "Forester", "2021")
print(myElectricCar.make)
print(myElectricCar.model)
print(myElectricCar.year)

print(myElectricCar.start())
print(myElectricCar.stop())
