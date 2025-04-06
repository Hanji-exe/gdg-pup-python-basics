# This program explores Python syntax, variables, data types, and basic operators.

# 1. Declare variables of different types
name = "Hanji"  # string
age = 19        # integer
weight = 55.63     # float
height = 5.5     # float
is_student = True  # boolean
is_working = False

# 2. Perform basic arithmetic operations
bmi = weight / (height * height) 
sum_result = weight + height
product_result = weight * height

# 3. Concatenate strings and display outputs
greeting = "Hello, " + name + "! You are " + str(age) + " years old and your BMI is " + str(round(bmi,2)) + "."
print(greeting)

# 4. Display results of arithmetic operations
print("Sum of weight and height:", sum_result)
print("Product of weight and height:", round (product_result,2))

# 5. Display the types of each variable
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of weight:", type(weight))
print("Type of height:", type(height))
print("Type of bmi:", type(bmi))
print("Type of is_student:", type(is_student))
print("Type of is_working:", type(is_working))