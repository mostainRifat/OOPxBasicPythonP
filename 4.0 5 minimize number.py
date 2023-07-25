def operations(N, arr):
    max = 0
    all_even = True

    for num in arr:
        if num % 2 != 0:
            all_even = False
            break

    if all_even:
        while all_even:

            arr = [x / 2 for x in arr]
            all_even = all(x % 2 == 0 for x in arr)

            if all_even:
                max += 1

    return max


N = int(input())
arr = list(map(int, input().split()))

result = operations(N, arr)
print(result)
