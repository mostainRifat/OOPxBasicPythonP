# Function is a first class object

def double_decker():
    print('Starting the double decker')
    def inner_fun():
        print('inside the inner')
        return 3000

    return inner_fun

# print(double_decker()())

def doSomething(work):
    print('work stated')
    #print(work)
    work()
    print('work ended')

# doSomething(3)
# doSomething('I am busy')

def coding():
    print('coding in python')
doSomething(coding)