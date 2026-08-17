# This file contains an review of the basic syntax of python, including variables, data type, etc.

def section_1():
    print("\n" "_________ 01_Variables ________ " "\n")
# Initializing variables
    name = "Teloxa"
    age = 22
    height = 1.80
    is_student = False

# Printing variables
    print(name, age, height, is_student, sep="\n")

def section_2():
    print("\n" "_________ 02_Data_Types ________ " "\n")
    # Demonstrating different data types
    
def section_3():
    print("\n" "_________ 01_Variables ________ " "\n")

# The dispatch table: number -> function reference (note: NO parentheses, we're not calling it yet)
SECTIONS = {
    1: section_1,
    2: section_2,
    3: section_3,
}

def run(section_number: int):
    func = SECTIONS.get(section_number)
    if func is None:
        raise ValueError(f"No section {section_number}. Available: {list(SECTIONS)}")
    func()

if __name__ == "__main__":
    run(1)  # <- Change this number to run a different section