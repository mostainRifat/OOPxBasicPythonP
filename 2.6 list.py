# list , array , collection is sample (simple terms)

#index =    0   1   2   3   4   5   6   7   8  9
numbers = [14, 27, 34, 47, 49, 56, 63, 71, 75, 87]
#index =  -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

#list (start : end)
#start from start index and stops before end index

print(numbers[3],numbers[-3])
print(numbers[2:6])

#list(start : end : step)
print(numbers[2:8:2])

print(numbers[7:2:-1])
print(numbers[4:])
print(numbers[:3])

print(numbers[::-1]) #shortcut of reverse