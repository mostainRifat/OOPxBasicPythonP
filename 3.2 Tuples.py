def multiple():
    return 3,4
#print(multiple())
things = 'pen','watch', 'light','glass', 'scale','phone','pen'
print(things[0])
print(things[-2])
print(things[3:6])

if 'phone' in things:
    print('exists')

for item in things:
    print (item)

#things = 'Sheet' # not support item assignment

print(len(things))\

mega  = ([2,3,4],[6,7,8,9])
#print(type(mega))
print(mega[0])
mega[0][1] = 666
print(mega)