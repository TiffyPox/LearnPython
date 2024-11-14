import random

# a main function (the entry point of a program) isn't required for Python
# it is common practice to define one for better organisation and readability

def main():
    print("Hello World")

# functions

firstName = "Tiffany"

def print_name():
    global secondName
    secondName = "Pottenger"

    print(firstName, secondName)

print_name()

# in Python, the data type is set when you assign a value to a variable
# if you want to specify the data type, use the following constructor functions

x = str("Hello World")
y = int(33)
z = dict(name="Jeff", age=33)

# a module is a file containing Python code, which can include functions, classes and variables:
# random is a module and for readability purposes, imports should be defined at the top of a program
print(random.randrange(1, 10))

# however, there are some instances where you might want to import within a function or a specific block of code
def my_math_function():
    import math
    print(math.sqrt(16))

my_math_function()

# this checks whether a Python script is being run directly or being imported as a module into another script
if __name__ == "__main__":
    main()


