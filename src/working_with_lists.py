def main():
    return 0

# Iterating through a list with a for loop
subjects = ["Science", "Maths", "Computing", "English"]

for subject in subjects:
    print(subject)

# Copying a list
original = [1, 2, 3, 4]

copy = original.copy()

copy.append(5)

print(original)
print(copy)

# Finding the min and max values
points = [22, 11, 98, 44, 222]

lowest = min(points)
highest = max(points)

print(lowest, highest)

# Concatenating two lists together using the + operator
first = [1, 2, 3]
second = [4, 5, 6]

combined = first + second
print(combined)

# Replicating a list multiple times using the * operator
repeated = first * 2
print(repeated)

# Checking if an element exists within a list using the 'in' and 'not in' operators
food = ["chips", "burger", "cake"]

if "cake" in food:
    print("Cake is in the list")

if "chocolate" not in food:
    print("Chocolate is not in the list")

if __name__ == '__main__':
    main()