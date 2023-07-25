def full_name(first,last):
    name = f'Fulll name : {first} {last}' #first+' '+last
    return name
#take parameters in order (serial wise)
#name = full_name('Alu' ,'dim')
name = full_name(last='Alu' , first='Dim')
print(name)

# def famous (** kargs)
def famous_name(first , last , **addition):
    name = f'{first} {last} '
    #print(additional['title'])
    for key, value in addition.items():
        print(key,value)
    return name

name = famous_name(first='Taher',last ='Ali',title='Hujor',last2='taheri')
print(name)

#def function_name(num1,num2,*args,**kargs):


#return multiple things from an array
def a_lot (num1 , num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1-num2
    return [sum,mult,remain]

everything = a_lot(25,35)
print (everything)
    