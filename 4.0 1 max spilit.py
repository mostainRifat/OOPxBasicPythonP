def split_string(S):
    count = 0
    count_L = 0
    count_R = 0

    balanced= []

    for char in S:
        if char == "L":
            count_L += 1
        else:
            count_R += 1

        if count_L == count_R:
            balanced.append(S[: count_L + count_R])
            S = S[count_L + count_R :]
            count += 1
            count_L = 0
            count_R = 0
    return count, balanced

S = input()
count, balanced = split_string(S)

print(count)
for string in balanced :
    print(string)
