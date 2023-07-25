# list -- []
# tuple --> ()
# set --> {}
# set: unique item collection

numbers = [12, 23, 32, 47, 53, 65, 23, 47]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)

numbers_set.add(55)
numbers_set.remove(65)
print(numbers_set)

if 12 in numbers_set:
    print("exists")
