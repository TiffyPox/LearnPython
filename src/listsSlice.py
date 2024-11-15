def main():
    return 0

# Slicing allows you to access a subset of elements in a list.
# The slice will include elements from the starting index up to, but not including the ending index

# Slicing lists
games = ['The Witcher', 'Satisfactory', 'Project Zomboid', 'Red Dead Redemption', '7 Days to Die']
print(games[1:4]) # Output would be 'Satisfactory', 'Project Zomboid', 'Red Dead Redemption'

print(games[:3]) # Output would be 'The Witcher', 'Satisfactory', 'Project Zomboid'

print(games[2:]) # Output would be 'Project Zomboid', 'Red Dead Redemption', '7 Days to Die'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers)

# Print a slice of the first five numbers
print(numbers[:5])

# Print a slice of the last five numbers
print(numbers[5:])

# Slicing the list with a step value (e.g. numbers [::2] to print every second element)
print(numbers[::3]) # Output would be 1, 4, 7, 10

if __name__ == '__main__':
    main()