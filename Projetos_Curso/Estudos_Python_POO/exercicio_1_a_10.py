from math import pi

# Disponível em: https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-1-create-a-class-with-instance-attributes
# Questão 1
class Vehicle():

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage   = mileage

#veiculo = Vehicle(100, 200)
#print(veiculo.max_speed, veiculo.mileage)

# Questão 2
class Vehicle():
    pass

# Questão 3
class Vehicle():

    def __init__(self, name, max_speed, mileage):
        self.name      = name
        self.max_speed = max_speed
        self.mileage   = mileage

class Bus(Vehicle):
    pass
    #def __init__(self, name, max_speed, mileage):
        # super(Vehicle, self).__init__(name = name, max_speed = max_speed, mileage = mileage)

ax = Bus('Volvo', 100, 200)
#print(ax.name, ax.max_speed,  ax.mileage)

# Questão 4
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    
    def ___init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity=50):
        # O super tem de vir antes da função que você quer modificar da classe anterior.
        return super().seating_capacity(capacity=50)
    
#carro = Bus("Volvo", 100, 200)
#print(carro.seating_capacity())

# Questão 5
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def color(self, color="white"):
        return "Color: White"
        
        
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

carro = Bus("Gol", 100, 200)
#print(f"{carro.color()}, Vehicle Name: {carro.name}, Speed: {carro.max_speed}, Mileage: {carro.mileage}")

# Questão 6
# Herança de classe, irei utilizar o "super" para obter a herança.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    
    def fare(self):
        amount = super().fare()
        amount += amount * (10/100)
        return amount

School_bus = Bus("School Volvo", 12, 50)
#print("Total Bus fare is:", School_bus.fare())

# Questão 7

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass
        

School_bus = Bus("School Volvo", 12, 50)
#print(type(School_bus))

# Questão 8
#print(isinstance(School_bus, Vehicle))

# Questão 9
class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

"""
print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))
print(issubclass(Cat, Animal))
print(issubclass(Puppy, Animal))
"""

# Questão 10
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        area_of_circle = (pi * (self.radius**2))
        return area_of_circle

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        area_of_square = (self.side**2)
        return area_of_square
    
# Example of polymorphism
shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(shape.area())  # Output: 78.53975, 49, 28.27431

