class Car :
    car_Count =0
    def __init__ (self ,model ,brand):
       self.__brand = brand
       self.__model = model
       Car.car_Count  +=1
    @staticmethod
    def total_Car():
       print(f"The total {Car.car_Count} is Created. ")  

    def get__brand(self):
       return self.__brand + " ..."
    
    @property
    def get__model(self):
       return self.__model + " ..."

    def getter (self):
       print(f"The car brand is {self.__brand}")
       print(f"The car model is {self.__model}")

class ElectricCar(Car):
   
   def __init__(self ,model ,brand,battery_size):
      super().__init__(model,brand)
      self.battery_size = battery_size

   def batterypack (self):
      print(f"The car Battery size is {self.battery_size}")
   
   def fuel_Type (self):
      print("Electricity")
   
class Hybrid_Car(ElectricCar):
   
   def __init__(self ,model ,brand,battery_size,fuel_type):
      super().__init__(model,brand,battery_size)
      self.fuel_type = fuel_type

   def fuel_type_info(self):
      print(f"The fuel type of Vehicle is {self.fuel_type}")
   
   def fuel_Type (self):
      print("This is the combination of both Petrol and Electricity")
      

my_car = Car("M5 Series","BMW")
print(my_car.get__model)


my_new_Ev = ElectricCar("model 3", "tesla" , "90KWH")
print(isinstance(my_new_Ev,Car))
print(isinstance(my_new_Ev,ElectricCar))
my_new_Ev.getter()
my_new_Ev.batterypack()
my_new_Ev.fuel_Type()

my_hybrid =Hybrid_Car("Aqua","Toyota", "25KWH", "Petrol")
my_hybrid.getter()
my_hybrid.fuel_type_info()
my_hybrid.fuel_Type()

print(my_hybrid.get__brand())
print(my_new_Ev.battery_size)
print(my_car.get__brand())

Car.total_Car()






class Battery :
   def __init__(self,battery_capacity):
      self.battery_capacity = battery_capacity
   def battery_Info(self):
      print("The battery capacity is : ",self.battery_capacity)

class Engine :
   def __init__(self,engine_cc):
      self.engine_cc = engine_cc
   def engine_Info(self):
      print("The Engine CCs  is : ",self.engine_cc)

class Hybrid_Car_Two(Battery,Engine):
   def __init__(self ,battery_capacity,engine_cc):
      Battery.__init__(self ,battery_capacity)
      Engine.__init__(self, engine_cc)
   
my_hybrid_car = Hybrid_Car_Two("25KWH ","1200cc")

my_hybrid_car.battery_Info()
my_hybrid_car.engine_Info()
      