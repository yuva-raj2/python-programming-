from abc import ABC,abstractmethod
class Vehicle(ABC):  #common methods #abstract class-imaginary implements the inherited class 
#You cannot create object for abstract class
#Classes inheriting abstract class must override all abstract methods
 @abstractmethod #decorator
 def start(self): #method 1
        pass
def stop(self):  #method 2
        pass
class Car(Vehicle): #concrete class-non abstract class It will have objects
 def start(self):   #method 1 Car vehicle
     print("You are riding a Car")
class Bike(Vehicle):
   def start(self):    #method 2 in bike vehicle
      print("You are riding a Bike")   