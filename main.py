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

#exercise 6 - Lists
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


#exercise 7 - Dictionaries
person = {"name": "Bob", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

#exercise 8 - Classes
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())

#exercise 9 - File Handling - TASK FOR USER TO COMPLETE
# with open("example.txt", "w") as file:
#     file.write("This is a sample text file.")
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)
