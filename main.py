#FreeCodeCamp python course - Basic Python Projects 

# ===== VARIABLES AND DATA TYPES =====
name = "David"
age = 22
is_student = True
height = 5.9  # Float (decimal number)
favorite_color = 'Blue'  # Single or double quotes work

# Print your variables
print("Name:", name)
print("Age:", age)
print("Is student:", is_student)
print("Height:", height)

# ===== STRING FORMATTING =====
# Different ways to format strings
print(f"\nHi, my name is {name} and I'm {age} years old.")
print("I am " + str(height) + " feet tall.")

# ===== BASIC MATH OPERATIONS =====
x = 10
y = 3

print(f"\nMath with {x} and {y}:")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Integer Division:", x // y)
print("Modulo (remainder):", x % y)
print("Power:", x ** y)

# ===== LISTS =====
# Lists can hold multiple values
colors = ["red", "blue", "green", "yellow"]
numbers = [1, 2, 3, 4, 5]

print("\nFirst color:", colors[0])  # Access by index (starts at 0)
print("Last color:", colors[-1])  # Negative index from end
print("All colors:", colors)

# List operations
colors.append("purple")  # Add to end
print("After append:", colors)

# ===== CONDITIONAL STATEMENTS =====
print("\n--- Conditionals ---")
if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor.")

# Multiple conditions
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score {score} = Grade {grade}")

# ===== LOOPS =====
print("\n--- Loops ---")

# For loop with range
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# For loop with list
print("Colors:")
for color in colors:
    print(f"- {color}")

# While loop
print("Countdown:")
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")

# ===== FUNCTIONS =====
def greet_person(person_name):
    """Function to greet someone"""
    return f"Hello, {person_name}! Welcome!"

def calculate_area(length, width):
    """Calculate rectangle area"""
    return length * width

# Using functions
greeting = greet_person(name)
print(f"\n{greeting}")

area = calculate_area(5, 3)
print(f"Area of 5x3 rectangle: {area}")

# ===== DICTIONARIES =====
student = {
    "name": "David",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.5
}

print("\nStudent Info:")
print("Name:", student["name"])
print("Major:", student["major"])
print("GPA:", student["gpa"])

# ===== USER INPUT =====
# Uncomment these lines to test user input:
# user_input = input("What's your favorite food? ")
# print(f"Cool! I like {user_input} too!")

# ===== PRACTICE EXERCISES =====
# Try these:
# 1. Create a list of your favorite movies
# 2. Write a function that calculates the area of a circle
# 3. Create a dictionary with your favorite book info

print("\n✅ Basic Python concepts covered!")
print("Run this file with: python main.py")
height = 5.9
