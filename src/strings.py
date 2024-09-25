def main():
    print("Hello World")

if __name__ == "__main__":
    main()

print("Hello")
print('Hello')

a = "World"

print(a)

# multiline strings
b = """Some people can't believe in themselves
until someone else believes in them first."""

c = '''Happiness can be found even in the darkest
of times, if one only remembers to turn on the light.'''

print("\n" + b + "\n\n" + c)

# square brackets can be used to access elements of a string:
print(b[1])

# since strings are arrays, we can loop through the characters in a string using a for loop:
for x in "banana":
    print(x)

# to get the length of a string:
print(len(b))

# use the 'in' keyword to check the string for a certain char or piece of text:
print("light" in c)

if "flower" not in c:
    print("The word flower is not in that sentence")