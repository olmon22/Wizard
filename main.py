"""
Comprehensive Python Course: From Basics to Intermediate
=======================================================

Welcome! This comprehensive course will guide you through Python programming, 
from basic concepts to intermediate-level topics and real-world applications.
"""

#==============================================================================
# 🟢 PYTHON BASICS
#==============================================================================

#------------------------------------------------------------------------------
# 1. Introduction to Python
#------------------------------------------------------------------------------
# Python is a popular, easy-to-learn programming language used for web development,
# data analysis, automation, scientific computing, AI, and more.

print("Hello, world!")  # Your first Python program

# To find your Python version
import sys
print(f"Python version: {sys.version}")

#------------------------------------------------------------------------------
# 2. Variables and Data Types
#------------------------------------------------------------------------------
# Variables store data. Python is dynamically typed.

# Basic data types
name = "Alice"      # String - text
age = 25            # Integer - whole numbers
height = 1.68       # Float - decimal numbers
is_student = True   # Boolean - True/False

print(f"Name: {name}, Age: {age}, Height: {height}m, Student: {is_student}")

# Type conversion
age_str = str(age)  # Convert integer to string
print(f"Age as string: {age_str}, Type: {type(age_str)}")

# Getting user input (uncomment to try)
# user_input = input("Enter your name: ")
# print(f"Hello, {user_input}!")

#------------------------------------------------------------------------------
# 3. Operators
#------------------------------------------------------------------------------
# Arithmetic operators
a, b = 10, 3
print(f"Addition: {a + b}")        # 13
print(f"Subtraction: {a - b}")     # 7
print(f"Multiplication: {a * b}")  # 30
print(f"Division: {a / b}")        # 3.3333...
print(f"Floor division: {a // b}") # 3
print(f"Modulus: {a % b}")         # 1
print(f"Exponentiation: {a ** b}") # 1000

# Comparison operators
print(f"Equal: {a == b}")          # False
print(f"Not equal: {a != b}")      # True
print(f"Greater than: {a > b}")    # True
print(f"Less than or equal: {a <= b}")  # False

# Logical operators
x, y = True, False
print(f"AND: {x and y}")  # False
print(f"OR: {x or y}")    # True
print(f"NOT: {not x}")    # False

# Assignment operators
c = 5      # Basic assignment
c += 3     # Same as: c = c + 3
print(f"c after += 3: {c}")  # 8

# Identity and membership
numbers = [1, 2, 3, 4, 5]
print(f"3 in numbers: {3 in numbers}")        # True
print(f"6 not in numbers: {6 not in numbers}")  # True

#------------------------------------------------------------------------------
# 4. Control Flow
#------------------------------------------------------------------------------
# if, elif, else statements
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is 5 or less")

# Nested conditions
y = 20
if x > 5:
    if y > 15:
        print("x > 5 and y > 15")
    else:
        print("x > 5 but y <= 15")

# Short-circuit evaluation
result = x > 5 and y > 15  # Both conditions are True
print(f"Result of x > 5 and y > 15: {result}")

#------------------------------------------------------------------------------
# 5. Loops
#------------------------------------------------------------------------------
# For loop
print("For loop with range:")
for i in range(3):  # 0, 1, 2
    print(f"Loop iteration {i}")

# For loop with collection
print("\nFor loop with list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Current fruit: {fruit}")

# While loop
print("\nWhile loop:")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# Loop control
print("\nLoop with break:")
for i in range(10):
    if i == 5:
        break  # Exit the loop
    print(i, end=" ")  # 0 1 2 3 4

print("\n\nLoop with continue:")
for i in range(5):
    if i == 2:
        continue  # Skip this iteration
    print(i, end=" ")  # 0 1 3 4

#------------------------------------------------------------------------------
# 6. Functions
#------------------------------------------------------------------------------
# Basic function
def greet(name):
    """This function greets the user by name."""
    return f"Hello, {name}!"

message = greet("Alice")
print(f"\n\n{message}")

# Parameters and arguments
def describe_person(name, age, city="Unknown"):
    """Function with default parameter"""
    return f"{name} is {age} years old and lives in {city}."

print(describe_person("Bob", 30, "New York"))
print(describe_person("Charlie", 25))  # Using default city

# Variable scope
global_var = "I'm global"

def scope_demo():
    local_var = "I'm local"
    print(f"Inside function - global: {global_var}, local: {local_var}")

scope_demo()
# print(local_var)  # This would cause an error - local_var is not defined globally

# Lambda functions (anonymous functions)
square = lambda x: x**2
print(f"Square of 5: {square(5)}")  # 25

#==============================================================================
# 🟡 PYTHON INTERMEDIATE
#==============================================================================

#------------------------------------------------------------------------------
# 7. Data Structures
#------------------------------------------------------------------------------
# Lists - ordered, changeable, allow duplicates
fruits = ["apple", "banana", "cherry", "apple"]
print(f"\nOriginal fruits list: {fruits}")

# List operations
fruits.append("orange")           # Add item
fruits.insert(1, "blueberry")     # Insert at position
fruits.remove("cherry")           # Remove item
popped_fruit = fruits.pop()       # Remove and return last item
print(f"Popped fruit: {popped_fruit}")
print(f"Modified fruits list: {fruits}")
print(f"List slice [1:3]: {fruits[1:3]}")  # Slicing

# Tuples - ordered, unchangeable, allow duplicates
coordinates = (10, 20, 30)
x, y, z = coordinates  # Unpacking
print(f"\nCoordinates tuple: {coordinates}")
print(f"Unpacked coordinates - x: {x}, y: {y}, z: {z}")

# Sets - unordered, unchangeable, no duplicates
unique_fruits = {"apple", "banana", "cherry", "apple"}
print(f"\nSet automatically removes duplicates: {unique_fruits}")

# Set operations
other_fruits = {"orange", "kiwi", "banana"}
print(f"Union: {unique_fruits.union(other_fruits)}")
print(f"Intersection: {unique_fruits.intersection(other_fruits)}")
print(f"Difference: {unique_fruits.difference(other_fruits)}")

# Dictionaries - key-value pairs
student = {
    "name": "Bob",
    "age": 20,
    "courses": ["Math", "Physics", "Computer Science"]
}

print(f"\nStudent dictionary: {student}")
print(f"Student name: {student['name']}")
print(f"Student's first course: {student['courses'][0]}")

# Dictionary methods
print(f"Dictionary keys: {list(student.keys())}")
print(f"Dictionary values: {list(student.values())}")
print(f"Get with default: {student.get('grade', 'Not Available')}")

#------------------------------------------------------------------------------
# 8. String Manipulation
#------------------------------------------------------------------------------
text = "Python programming is fun!"
print(f"\nOriginal text: {text}")

# String methods
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Replace: {text.replace('fun', 'amazing')}")
print(f"Split: {text.split()}")
print(f"Count 'i': {text.count('i')}")
print(f"Find 'prog': {text.find('prog')}")

# String formatting
name, age = "David", 35
# f-strings (Python 3.6+)
print(f"{name} is {age} years old.")
# format() method
print("{} is {} years old.".format(name, age))
# % formatting (older style)
print("%s is %d years old." % (name, age))

#------------------------------------------------------------------------------
# 9. File Handling
#------------------------------------------------------------------------------
# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, file!\n")
    f.write("This is a new line.\n")
    f.write("Python file handling is straightforward.\n")

# Reading from a file
print("\nReading file:")
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line
print("\nReading line by line:")
with open("example.txt", "r") as f:
    for line in f:
        print(f"Line: {line.strip()}")

# Appending to a file
with open("example.txt", "a") as f:
    f.write("This line was appended.\n")

#------------------------------------------------------------------------------
# 10. Exception Handling
#------------------------------------------------------------------------------
print("\nException handling examples:")

# Try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

# Try-except-else-finally
try:
    value = int("10")
except ValueError:
    print("That's not a valid number!")
else:
    print(f"Conversion successful: {value}")
finally:
    print("This always executes.")

# Handling multiple exceptions
try:
    value = int("abc")
    result = 10 / value
except ValueError:
    print("Invalid conversion to integer.")
except ZeroDivisionError:
    print("Division by zero!")
except Exception as e:
    print(f"Other error: {e}")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

#------------------------------------------------------------------------------
# 11. Modules and Packages
#------------------------------------------------------------------------------
# Importing built-in modules
import math
print(f"\nPi value: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

# Importing specific functions
from random import randint, choice
print(f"Random number between 1 and 10: {randint(1, 10)}")
print(f"Random choice from list: {choice(['red', 'green', 'blue'])}")

# Module aliases
import datetime as dt
today = dt.date.today()
print(f"Today's date: {today}")

# Creating a custom module
# In a real scenario, you would create a separate file (e.g., mymodule.py)
# For demonstration, we'll create a string representation of a module
custom_module = """
def say_hello(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

PI = 3.14159
"""

# For demonstration purposes - normally, you'd import the file
print("\nCustom module would contain functions like say_hello() and add_numbers()")

#------------------------------------------------------------------------------
# 12. List Comprehensions
#------------------------------------------------------------------------------
# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"\nSquares using list comprehension: {squares}")

# With condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# With if-else
results = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Even/odd labels: {results}")

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

#------------------------------------------------------------------------------
# 13. Working with Dates and Time
#------------------------------------------------------------------------------
from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(f"\nCurrent date and time: {now}")
print(f"Formatted date: {now.strftime('%Y-%m-%d')}")
print(f"Formatted time: {now.strftime('%H:%M:%S')}")
print(f"Custom format: {now.strftime('%A, %B %d, %Y')}")

# Date calculations
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

one_week_ago = now - timedelta(weeks=1)
print(f"One week ago: {one_week_ago.strftime('%Y-%m-%d')}")

# Parsing dates
date_string = "2023-01-15"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")

#------------------------------------------------------------------------------
# 14. Working with JSON
#------------------------------------------------------------------------------
import json

# Dictionary to JSON string
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "languages": ["Python", "JavaScript", "SQL"],
    "is_employee": True
}

# Serializing (dict to JSON string)
json_string = json.dumps(person, indent=4)
print(f"\nJSON string:\n{json_string}")

# Writing JSON to a file
with open("person.json", "w") as f:
    json.dump(person, f, indent=4)

# Reading JSON from a file
with open("person.json", "r") as f:
    loaded_person = json.load(f)
    print(f"Loaded from JSON file: {loaded_person}")

# Deserializing (JSON string to dict)
decoded = json.loads(json_string)
print(f"Decoded JSON - name: {decoded['name']}, languages: {decoded['languages']}")

#==============================================================================
# 🟠 OBJECT-ORIENTED PROGRAMMING (OOP)
#==============================================================================

#------------------------------------------------------------------------------
# 15. Classes and Objects
#------------------------------------------------------------------------------
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor method
    def __init__(self, name, age):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance methods
    def bark(self):
        return f"{self.name} says Woof!"
    
    def description(self):
        return f"{self.name} is {self.age} years old"

# Creating objects (instances)
buddy = Dog("Buddy", 3)
max = Dog("Max", 5)

print(f"\nDog 1: {buddy.name}, Age: {buddy.age}, Species: {buddy.species}")
print(f"Dog 2: {max.name}, Age: {max.age}, Species: {max.species}")
print(buddy.bark())
print(max.description())

#------------------------------------------------------------------------------
# 16. OOP Concepts
#------------------------------------------------------------------------------
# Inheritance
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        return "Some generic animal sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

class Cat(Animal):  # Cat inherits from Animal
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, species="Cat")
        self.breed = breed
        
    # Override method
    def make_sound(self):
        return "Meow!"
    
    # Add new method
    def purr(self):
        return f"{self.name} is purring..."

# Create an instance of derived class
whiskers = Cat("Whiskers", "Siamese")
print(f"\n{whiskers.info()}, Breed: {whiskers.breed}")
print(f"Sound: {whiskers.make_sound()}")
print(whiskers.purr())

# Encapsulation - using naming conventions (no true private variables in Python)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner      # Public attribute
        self._balance = balance  # Protected attribute (convention)
        
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Invalid withdrawal amount"
    
    def get_balance(self):
        return f"Balance for {self.owner}: ${self._balance}"

account = BankAccount("Alice", 100)
print(f"\n{account.get_balance()}")
print(account.deposit(50))
print(account.withdraw(30))

# Polymorphism - same method name, different behaviors
animals = [Animal("Generic", "Animal"), Dog("Rex", 4), Cat("Felix", "Tabby")]

print("\nPolymorphism example:")
for animal in animals:
    print(f"{animal.name} says {animal.make_sound()}")

#------------------------------------------------------------------------------
# 17. Special Methods
#------------------------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # String representation for developers
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    # String representation for users
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # Calculate length (distance from origin)
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)
    
    # Equality comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Addition operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"\nPoint representation: {p1}")  # Calls __str__
print(f"Developer representation: {repr(p1)}")  # Calls __repr__
print(f"Length of p1: {len(p1)}")  # Calls __len__
print(f"p1 == p3: {p1 == p3}")  # Calls __eq__
print(f"p1 + p2: {p1 + p2}")  # Calls __add__

#==============================================================================
# 🔵 INTERMEDIATE REAL-WORLD CONCEPTS
#==============================================================================

#------------------------------------------------------------------------------
# 18. Working with Virtual Environments
#------------------------------------------------------------------------------
print("\n# Virtual Environments")
print("""
# In terminal:
# Create: python -m venv myenv
# Activate (Windows): myenv\\Scripts\\activate
# Activate (macOS/Linux): source myenv/bin/activate
# Deactivate: deactivate
# Install packages: pip install package_name
# Requirements file: pip freeze > requirements.txt
# Install from requirements: pip install -r requirements.txt
""")

#------------------------------------------------------------------------------
# 19. Using External Libraries
#------------------------------------------------------------------------------
print("# External Libraries")
print("""
# Install with pip:
# pip install requests pandas matplotlib

# Example of using requests library:
import requests
# response = requests.get("https://api.example.com/data")
# print(response.json())

# Example of using pandas:
import pandas as pd
# df = pd.read_csv("data.csv")
# print(df.head())

# Example of using matplotlib:
import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
# plt.title("Simple Plot")
# plt.show()
""")

#------------------------------------------------------------------------------
# 20. Introduction to Python Testing
#------------------------------------------------------------------------------
print("# Testing in Python")
print("""
# Basic assertions
assert 1 + 1 == 2, "1 + 1 should equal 2"

# Using unittest framework
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        
# Run tests with: python -m unittest test_module.py
""")

#------------------------------------------------------------------------------
# 21. Decorators
#------------------------------------------------------------------------------
# Function decorator
def timer(func):
    """A decorator that prints how long a function took to run"""
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to run.")
        return result
    return wrapper

@timer
def slow_function():
    """A function that simulates a slow operation"""
    import time
    time.sleep(0.1)  # Sleep for 0.1 second
    return "Function completed"

print("\n# Decorators Example:")
result = slow_function()
print(result)

# Class methods and static methods
class MathUtils:
    @staticmethod
    def add(a, b):
        """Static method doesn't need a class instance"""
        return a + b
        
    @classmethod
    def multiply(cls, a, b):
        """Class method receives the class as first argument"""
        print(f"Using {cls.__name__}")
        return a * b

print(f"Static method: {MathUtils.add(5, 3)}")
print(f"Class method: {MathUtils.multiply(5, 3)}")

#------------------------------------------------------------------------------
# 22. Generators and Iterators
#------------------------------------------------------------------------------
# Generator function using yield
def fibonacci(n):
    """Generate Fibonacci sequence up to n numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("\n# Generator example - Fibonacci sequence:")
for num in fibonacci(10):
    print(num, end=" ")

# Generator expressions
print("\n\n# Generator expression:")
numbers = [1, 2, 3, 4, 5]
squared_gen = (x**2 for x in numbers)  # Generator expression
print(f"Generator object: {squared_gen}")
print(f"First value: {next(squared_gen)}")
print(f"Remaining values: ", end="")
for val in squared_gen:
    print(val, end=" ")

print("\n\nCongratulations! You've completed a comprehensive Python course covering basics to intermediate concepts.")
"""
def main():