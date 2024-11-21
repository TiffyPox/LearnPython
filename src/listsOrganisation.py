def main():
    return 0

# Sorting a list
nums = [4, 7, 2, 1, 99, 23, 55, 6]

nums.sort()

print(nums)

# Creating a new sorted list
unsorted_nums = [66, 3, 22, 46, 9, 21, 53, 12]
sorted_nums = sorted(unsorted_nums)

print(unsorted_nums)
print(sorted_nums)

# Reversing a list
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

days.reverse()

print(days)

# Returning the first occurrence of a specified element
flowers = ["rose", "daisy", "tulip"]

pos = flowers.index("daisy")
print(pos)

# Returning the number of times a specified element appears
nums = [5, 5, 4, 3, 2, 1, 5]

count = nums.count(5)
print(count)

# Python sorts a list of strings alphabetically by default
names = ["Dave", "Adam", "Brian", "Colin"]

names.sort()
print(names)

if __name__ == '__main__':
    main()