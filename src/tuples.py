def main():
    return 0

# Unlike lists, tuples are immutable, meaning they cannot be modified after creation
# Tuples are useful when you want to store data that should not change during the program

dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

# When defining a tuple with a single element, make sure to add the trailing comma
single_tuple = (5,)

print(type(single_tuple))

not_a_tuple = (5)

print(type(not_a_tuple))

# Looping through a tuple
for dimension in dimensions:
    print(dimension)

# Modifying tuples by reassignment
menu = ("chips", "pasta", "cake")

menu = ("fish", "spaghetti", "toast")

print("Modified menu:", menu)

if __name__ == '__main__':
    main()