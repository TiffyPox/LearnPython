def main():

    nums = [1, 2, 3, 4]

    print("Guess 4 numbers between 0-9 separated with a space:")

    guesses = []

    already_guessed = []

    response = (input())

    guesses = response.split()

    for i in range(len(guesses)):
        guesses[i] = int(guesses[i])

    print(f"Your numbers are: {guesses}")

    for i in range(len(guesses)):
        already_guessed.append(guesses[i])

        if guesses[i] == nums[i]:
            print("Y")  # Number and position is correct
        elif guesses[i] in nums:
            print("N")  # Number is correct but wrong place
        else:
            print("X")  # Number is incorrect

    print(f"\nNumbers you have already guessed: {already_guessed}")

    print("Guess 4 numbers between 0-9 separated with a space:")

    response = (input())

    guesses = response.split()

    for i in range(len(guesses)):
        guesses[i] = int(guesses[i])

    print(f"Your numbers are: {guesses}")

    for i in range(len(guesses)):
        already_guessed.append(guesses[i])

        if guesses[i] == nums[i]:
            print("Y", end=" ")  # Number and position is correct
        elif guesses[i] in nums:
            print("N", end=" ")  # Number is correct but wrong place
        else:
            print("X", end=" ")  # Number is incorrect

    print(f"\nNumbers you have already guessed: {already_guessed}")

    print("Guess 4 numbers between 0-9 separated with a space:")

if __name__ == '__main__':
    main()