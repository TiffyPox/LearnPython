def main():
    print("Hello World")

# Function to reverse a string
def reverse_string(s):
    return(s[::-1])

my_string = "Hello my name is Tiffany"
final = reverse_string(my_string)
print(final)

# Entry point:
if __name__ == "main":
    main()