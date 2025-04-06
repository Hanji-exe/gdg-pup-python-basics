class car:
    def __init__ (self,make, model, year, color):
          self.make = make
          self.model = model
          self.year = year
          self.color = color
          
    def describe(self):
          return f"This car is a {self.color} {self.year} {self.make} {self.model}."

# OPTIONAL:  ginawa ko na lang siyang user input para mas interactive po siya hehe
model = input("Enter the car model: ")
year = int(input("Enter the car year: "))
make = input("Enter the car brand: ")
color = input("Enter the car color: ")

myCar = car((make), (model), (year),(color))
print(myCar.describe())
            