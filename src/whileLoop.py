def main():
    print("Hello World")

i = int(1)

while i < 11:
    print(i)
    i += 1

# Using break to exit the loop:
j = int(1)

while j < 6:
    print(j)
    if j == 3:
        break
    j += 1

# Using continue to stop the current iteration and continue:

k = int(0)

while k < 6:
    k += 1
    if k == 3:
        continue # skips three
    print(k)

# Using the else statement:

l = int(1)

while l < 11:
    print(l)
    l += 1
else:
    print("Variable is no longer less than 11")

if __name__ == "__main__":
    main()