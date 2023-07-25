numbers = [12, 23, 32, 47, 53, 65, 23, 47] 
person = ['kala chan','kalurghat',23,'student']

#key value pair
#dictionary
#object
#overlap with set
#{key : value , key : value}
#mutable

person = {'name':'kala pakhi' , 'add' : 'Kalurghat' , 'age' : 23 , 'job' : 'booker'}
print (person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
del person['age']
print(person)

for key,value in person.item():
    print(key,value)