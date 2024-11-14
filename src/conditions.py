def main():
    print("Hello World")

x = int(30)
y = int(33)
z = int(33)

if x > y:
    print(str(x) + " is more than " + str(y))
elif y > x:
    print(str(y) + " is more than " + str(x))

if y > z:
    print(str(y) + " is more than " + str(z))
elif z > y:
    print(str(z) + " is more than " + str(y))
else:
    print("Both " + str(y) + " and " + str(z) + " are equal")

# if there is just one if and one else, you can put them both on the same line:
print(str(x) + " is more than " + str(y)) if x > y else print(str(y) + " is more than " + str(x))

# using the and operator:
if x < z and y > x:
    print("Both conditions are true")

# using the or operator:
if x > z or y > x:
    print("One of the conditions is true")

# using the not operator:
if not x > y:
    print(str(x) + " is NOT greater than " + str(y))

if __name__ == "__main__":
    main()
