def main():
    print()

import random

# Design an algorithm that generates a series of 100 random values between 1-10
# Allow the user to enter a value 
# The program will state how many times that number occurs in the random series

random_series = []

for i in range(100):
    random_series.append(random.randrange(1, 10))

print(random_series)

user_num = int(input("Please enter a number: "))

def num_frequency(n, num_list):
    count = 0
    
    for num in num_list:
        if (num == n):
            count += 1

    return count

result = num_frequency(user_num, random_series)

print(f"Your number showed up {result} times in my series of random numbers!")

# The time complexity of this program is O(n) because the loop only runs once for each element in the num_list
# The loop executes n times

if __name__ == '__main__':
    main()