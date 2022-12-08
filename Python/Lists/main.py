# Write a program in Python with different list examples.

import random

numbers = [random.randint(-100, 500) for _ in range(random.randint(5, 15))]


def function(x):
    return list(dict.fromkeys(x))


# min_list
def min_list(list):
    min_num = list[0]
    for num in list:
        if num < min_num:
            min_num = num
    return min_num


# max_list
def max_list(list):
    max_num = list[0]
    for num in list:
        if num > max_num:
            max_num = num
    return max_num


# sum_list
def sum_list(list):
    sum = 0
    for num in list:
        sum = sum + num
    return sum


# odd_list
def odd_list(list):
    odds = []
    for num in list:
        if num % 2 != 0:
            odds.append(num)
    return odds


print(numbers)
print("Minimum number is:", min_list(numbers), ".")
print("Max number is:", max_list(numbers), ".")
print("Sum is:", sum_list(numbers), ".")
print("Average is:", sum_list(numbers) / len(numbers), ".")
print("Odd numbers are:", odd_list(numbers), ".")
