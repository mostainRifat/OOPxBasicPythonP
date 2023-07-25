def sum(num1, num2):
    result = num1 + num2
    return result


total = sum(33, 17)
# print = ('Total ',total)

# ARGS


def all_sum(num1,num2, *numbers):
    print(numbers)
    sum =0
    for num in numbers:
        print(num)
        sum = sum+num
    return sum


total = all_sum(35, 45, 55, 15,25)
print("All Sum :", total)

#def doSomethin(*args):
    #print (args)
