N, M = map(int, input().split())
nums = list(map(int, input().split()))

occurance = {}

for num in nums :
    if num in occurance:
        occurance[num] += 1
    else :
        occurance [num ] =1

result = []

for i in range (1, M+1):
    print (occurance.get(i,0))