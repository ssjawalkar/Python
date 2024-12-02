# Single Inheritance Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}, and I am {self.age} years old."

class Employee(Person):  # Single inheritance
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def work(self):
        return f"{self.introduce()} I am working with Employee ID: {self.employee_id}."

# Multiple Inheritance Example
class Flyer:
    def fly(self):
        return "Can fly high in the sky."

class Programmer:
    def code(self):
        return "Can write efficient code."

class TechPilot(Flyer, Programmer):  # Multiple inheritance
    def multitask(self):
        return f"{self.fly()} and {self.code()}"  

# Multilevel Inheritance Example
class Device:
    def __init__(self, name):
        self.name = name

    def power_on(self):
        return f"{self.name} is powered on."

class Phone(Device):
    def make_call(self):
        return f"{self.power_on()} It can make a call."  

class Smartphone(Phone):  # Multilevel inheritance
    def browse_internet(self):
        return f"{self.make_call()} It can also browse the internet."  

# Single Inheritance
employee = Employee("Bob", 35, "E12345")
print(employee.work()) 

# Multiple Inheritance
tech_pilot = TechPilot()
print(tech_pilot.multitask()) 

# Multilevel Inheritance
smartphone = Smartphone("iPhone")
print(smartphone.browse_internet())  

