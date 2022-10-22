# Make an iterable list in Python.

fruits = ["apple", "orange", "kiwi"]

# Iterator object
iterator_object = iter(fruits)

# Infinite while loop
while True:
    try:
        fruit = next(iterator_object)
        print(fruit)
    except StopIteration:
        break
