# This is the class called Dog
class Dog:
    def __init__(self, name):
        self.name = name

    # This is a function that the class Dog can perform
    def bark(self):
     return "Woof!"

# Create an instance (an object) of Dog
dog = Dog("Rex")

# Call the function that dog can perform
print(dog.bark())

# Output is: "Woof!"

