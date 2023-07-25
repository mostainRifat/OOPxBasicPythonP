import math 
import time

def timer(func):
    def inner(*args , **kargs):
        print('Time Started')
        start = time.time()
        #print(func)
        func(*args , ** kargs)
        print('Time Ended')
        end = time.time()
        print(f'Total Time Taken {end - start}')

    return inner

@timer
def getFactorial(n):
    print('factorial Starting')
    result = math.factorial(n)
    print(f'Factorial of {n} is : {result}')

getFactorial(120)
#timer()()