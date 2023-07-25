# lambda

# def doubled (x):
#     return x*2

doubled = lambda num : num * 2
squared = lambda num : num*num

result = doubled(33)
output = squared (4)

print(result, output)

add = lambda x,y : x+y

sum = add (19,22)
print(sum)

numbers = [12, 23, 32, 47, 53, 65, 23, 47]

#doubled_nums = map (doubled, numbers)
doubled_nums  =  map (lambda x: x*2 , numbers)
print(list (doubled_nums) )

squared_nums = map (lambda x: x*x , numbers)
print(list(squared_nums))

actors = [
    {'name' : 'sabana', 'age' : 65},
    {'name' : 'sabnur', 'age' : 45},
    {'name' : 'sabila', 'age' : 30},
    {'name' : 'srabonti', 'age' : 37},
    {'name' : 'safa', 'age' : 30},

]

juniors = filter (lambda actor : actor['age']< 40, actors)

print(list(juniors))
