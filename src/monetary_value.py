# Write a program that takes input from the user 
# The output should be the minimum amount of pennies required to represent that number in monetary value
# e.g. 25 = 20p, 5p

def main():
    num = int(input("Please enter a number: "))
    result = get_coins(num)
    print(result)

# List of coins available
coin_values = [1, 2, 5, 10, 20, 50, 100, 200]
coins = {1: "1p", 2: "2p", 5: "5p", 10: "10p", 20: "20p", 50: "50p", 100: "£1", 200: "£2"}

# Sort coin_values in descending order to ensure the best solution
# If the list wasn't sorted, the program would pick the smallest coins first
coin_values.sort(reverse = True)

def get_coins(n):
    if n in coins:
        return(f"To represent the number {n} in monetary value, you would need the following coins: {coins[n]}")
    else:
        return find_min(n)

def find_min(n):
    num = n
    coin_list = []
    
    for coin in coin_values:
        while n >= coin:
            n -= coin
            coin_list.append(coins[coin])

    return (f"To represent {num} in monetary value, you would need the following coins: {', '.join(coin_list)}")

# The time complexity of this program is O(n)

if __name__ == "__main__":
    main()