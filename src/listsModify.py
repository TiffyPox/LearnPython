def main():
    return 0

# List in Python are mutable, meaning you can modify elements after creating the list
animals = ['zebra', 'panda', 'monkey']
print(animals)

# Update elements in a list
animals[1] = 'jellyfish'

# Print the updated list to see if the change was successful
print(animals)

# Reversing the contents of a list
nums = [1, 2, 3, 4, 5]

nums.reverse()

print(nums)

# Adding elements to a list
furniture = ['chair', 'desk', 'sofa']

# Using the 'append' function to add an element to a list:
furniture.append('bed')
print(furniture)

food = ['burger', 'chips', 'pasta']

# Using the 'insert' function to add an element to a list:
food.insert(0, 'salad') # Adds 'salad' at index 0

print(food)

# Removing elements from a list

# Removing elements with the remove() function:
drinks = ['Pepsi', 'Water', 'Fanta', 'Juice']

drinks.remove('Pepsi') # Removes the first occurrence of Pepsi

print(drinks)

# Removing elements using the pop() function:
drinks.pop(1) # Removes the element at index 1

print(drinks)

# Using the del() function:
del drinks[0] # Deletes the first element

print(drinks)

if __name__ == '__main__':
    main()