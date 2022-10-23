# Write a function in Python called max_list that accepts a list as an argument and returns the maximum number in that list.
# Write a function in Python called sum_list that accepts a list as an argument and returns the sum of all the numbers in that list.
# Write a function in Python called odds_list that accepts a list as an argument and returns a new list with only the odd numbers from the list passed in.

import random

nums = [random.randint(-100, 500) for _ in range(random.randint(5, 15))]


def myfunc(x):
    return list(dict.fromkeys(x))


def min_list(list):
    min_num = list[0]
    for num in list:
        if num < min_num:
            min_num = num
    return min_num


# max_list function
def max_list(list):
    max_num = list[0]
    for num in list:
        if num > max_num:
            max_num = num
    return max_num


# sum_list function
def sum_list(list):
    sum = 0
    for num in list:
        sum = sum + num
    return sum


# odd_list function
def odd_list(list):
    odds = []
    for num in list:
        if num % 2 != 0:
            odds.append(num)
    return odds


print(nums)

print("Minimum number is:", min_list(nums))

print("Max number is:", max_list(nums))

print("Sum is:", sum_list(nums))

print("Average is:", sum_list(nums) / len(nums))

print("Odd numbers are:", odd_list(nums))
