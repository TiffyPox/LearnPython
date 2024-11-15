def main():
    print("Hello World")

# Lists
x = ["Apple", "Banana", "Orange"]
a, b, o = x

print(a + " " + b + " " + o)

# Nested List
y = [1, 2,[3, 4],[5,[100, 200,['Hello']],23,11],1,7]

print(y[3][1]) # prints [100, 200 ['Hello']]

print(y[3][1][2]) # prints ['Hello']

print(y[3][1][2][0]) # prints Hello

z = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(z['k1'][3]['tricky'][3]['target'][3]) # prints hello

family_members = ["Bob","Jude",["Aunt",["Cat","Dog"]]]

print(family_members[2][1][0]) # prints Cat

# get the length (prints 2)
print(len(family_members[2][1]))

jewellery = ['Necklace', 'Earrings', 'Watch', 'Ring', 'Bracelet']

print(len(jewellery)) # Output would be 5

# using list comprehension to create a new list:
numbers = [1, 2, 3, 4, 5]

squares = [n**2 for n in numbers]

print(squares) # Output would be 1, 4, 9, 16, 25

odds_and_evens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# using list comprehension to create a new list that contains only the even numbers
even_numbers = [n for n in odds_and_evens if n%2 == 0 ]

print(even_numbers)

if __name__ == "__main__":
    main()