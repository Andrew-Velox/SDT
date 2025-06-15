# Q:1
# Write what is meant by operator overloading and method overriding with examples.
# Operator Overloading in Python
# ----------------------------------------------------------------
'''class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1) # Output: (2, 3)
print(v2) # Output: (4, 5)
v3 = v1 + v2  # Calls v1.__add__(v2)
print(v3)     # Output: (6, 8) '''


# Method Overriding in Python

'''class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):  # Overrides parent method
        print("Dog barks")

a = Animal()
d = Dog()

a.sound()  # Output: Animal makes a sound
d.sound()  # Output: Dog barks '''
# ----------------------------------------------------------------
# Q:2
'''
class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)
    
    def __lt__(self, other):
        return self.age < other.age

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)

# Find out which of these players is older using the operator overloading.

players = [sakib, musfiq, kamal, jack, kalam]

older = players[0]
for player in players:
    if player > older:
        older = player

print(older.name, older.age) # Output: kamal 39 '''

# ----------------------------------------------------------------
# Q:3
# Write down 4 differences between the class method and static method with proper examples.
'''
# Source: GFG
Class method vs Static Method
The difference between the Class method and the static method is:

A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can't access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

''' 
# ------------------------------------------------------------------
# Q:4
# Write what are getter and setter with proper examples
'''


Getter: A method used to get (access) the value of a private attribute.
Setter: A method used to set (modify) the value of a private attribute.


Why Use Getters and Setters?
    Encapsulation: Keep attributes private (__attribute)
    Validation: Check input before updating a value
    Control: Add logic when getting or setting data

    # CODE EXAMPLE:

class Person:
    def __init__(self, name, age):
        self.__name = name       # private attribute
        self.__age = age

    @property
    def age(self):              # Getter method
        return self.__age

    @age.setter
    def age(self, value):       # Setter method
        if value >= 0:
            self.__age = value
        else:
            print("Age can't be negative!")


p = Person("John", 25)
print(p.age)     # calls getter → Output: 25

p.age = 30       # calls setter → age updated
print(p.age)     # Output: 30

p.age = -5       # Output: Age can't be negative!


'''

# ------------------------------------------------------------------
# Q:5
# Explain the difference between inheritance and composition with proper examples.
'''
| Feature            | Inheritance                     | Composition                                 |
| ------------------ | ------------------------------- | ------------------------------------------- |
| Relationship Type  | "Is-a"                          | "Has-a"                                     |
| Coupling           | Tightly coupled                 | Loosely coupled                             |
| Flexibility        | Less flexible (fixed hierarchy) | More flexible (can combine behaviors)       |
| Reusability        | Inherits everything from parent | Can choose which objects to include         |
| Multiple Behaviors | Limited by base classes         | Can combine many objects of different types |


# Example of Inheritance---------

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Inheritance: Dog *is an* Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()   # Output: Animal speaks
d.bark()    # Output: Dog barks

# Example of Composition------------

class Engine:
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car *has an* Engine

    def drive(self):
        self.engine.start()
        print("Car is driving")

c = Car()
c.drive()
# Output:
# Engine starts
# Car is driving

'''
