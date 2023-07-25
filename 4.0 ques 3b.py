def add (*number):
    total = 0 
    for num in number:
        total = total + num
    return total

print(add(5,6))

def total_fruits(**kwargs):
    print(kwargs, type(kwargs))


total_fruits(banana=3, mango=9, watermelon=8)