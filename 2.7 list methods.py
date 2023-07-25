numbers = [23,45,95,67,83]
numbers.append(91)
print(numbers)

numbers.insert(3,71)
print(numbers)

if 6 in numbers:
    numbers.remove(6)
print(numbers)

last = numbers.pop()
print(last , numbers)

if 71 in numbers:
    index= numbers.index(71)
    print(index)

Sorted= numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)