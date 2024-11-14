from string import ascii_lowercase

# A function that determines if a string contains all the letters in the alphabetS
def check_string(s):
    # Your code goes here
    missing = []

    for letter in ascii_lowercase:
        if letter not in s.lower():
            missing.append(letter)

    new_list = missing

    if len(missing) > 0:
        return(f"The string is missing the following letters: {''.join(missing)}")
    else:
        return("The string contains all the letters of the alphabet.")

def main():
    print("Hello World")

    # Checking if two strings contain all the letters in the alphabet
    str1 = "abcdeghijklnopqrsuvwxy"
    str2 = "abcdefghijklmnopqrstuvwxyz"

    print(check_string(str1))
    print(check_string(str2))

if __name__ == '__main__':
    main()