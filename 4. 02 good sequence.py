def removedElement(n, a):
    total = 0
    processed = set()

    for num in a:
        
        if num <= n and num not in processed:
            #print (a.count(num))
            if a.count(num) > num :
                total += a.count(num) - num
                processed.add(num)
            
            elif a.count(num) != num:
                total += 1 

    return total


n = int(input())
a = []
for _ in range(0, n):
    element = int(input())
    a.append(element)

answer = removedElement(n, a)
print(answer)
