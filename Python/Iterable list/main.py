# Make an iterable list in Python.

fruits = ["apple", "orange", "kiwi"]

iterator_object = iter(fruits)

while True:
    try:
        fruit = next(iterator_object)
        print(fruit)
    except StopIteration:
        break
