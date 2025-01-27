def main():
    print()

# Computational thinking, algorithms and complexity
# Implement an algorithm that calculates x(n) (x raised to the power of n)
# e.g 2(x), 4(n) 2 x 2 x 2 x 2 = 16(answer)

def calculate(x, n):
    answer = x

    for i in range(1, n):
        answer = answer * x
    
    return answer

x = float(input("x variable:")) # Base number
n = int(input("n variable:")) # Exponent

answer = calculate(x, n)
print(answer)


# The time complexity of the above program is O(n) (linear complexity)

# Modify the algorithm so that is deals with any values of n that are positive and negative ints
def modified_calculation(x, n):
    # If n is 0
    if n == 0:
        if x == 0:
            print("Cannot perform calculation as both inputs are 0")
        else:
            return 1
    
    # If n is positive
    elif n > 0:
        modified_answer = 1
        for i in range(n):
            modified_answer *= x

        return modified_answer
    
    # If n is negative
    else:
        modified_answer = 1
        for i in range(-n):
            modified_answer *= x

        return 1 / modified_answer
    
modified_answer = modified_calculation(x, n)
print(modified_answer)

# The time complexity of the above modified program is O(|n|)
# This means that the runtime depends on the absolute value of n
# The absolute value of n is the non-negative value of n

if __name__ == '__main__':
    main()