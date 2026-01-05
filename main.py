#FreeCodeCamp - Introduction to python 

#exercise 1 - Hello World

print("Hello, World!")

#exercise 2 - Variables and Data Types
name = "Alice"
age = 30
is_student = False
print(f"Name: {name}, Age: {age}, Is Student: {is_student}")

#exercise 3 - Control Flow
if age >= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.")

#exercise 4 - Loops
for i in range(5):
    print(f"Iteration {i+1}")


#exercise 5 - Functions
def greet(person_name):
    return f"Hello, {person_name}!"
print(greet(name))