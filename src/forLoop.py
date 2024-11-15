def main():
    print("Hello World")

# iterating through a list:
x = ["Apple", "Banana", "Orange"]

for fruit in x:
    print(fruit)

# modify the loop to print a message with each item
for fruit in x:
    print(f"I love {fruit}s!")

# iterating through a string to print the characters:
y = str("Tiffany")

for ltr in y:
    print(ltr)

# using the continue and break statements:
x.insert(3, "Cherry")
x.insert(4, "Strawberry")

print("Shopping list updated!")

for fruit in x:
    if fruit == "Orange":
        break
    print(fruit)

for fruit in x:
    if fruit == "Cherry":
        continue
    print(fruit)

# using the range() function:
for x in range(5):
    print(x)

# nested loop:
feeling = ["Good", "Bad", "Great"]
time_of_day = ["Morning", "Afternoon", "Evening"]
for x in feeling:
    for y in time_of_day:
        print(x,y)

# for loops shouldn't be empty but in the event that they are, use the pass statement:
for x in [0, 1, 2]:
    pass

if __name__ == '__main__':
    main()