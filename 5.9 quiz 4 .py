class A:
    def __init__(self, value):
        value = 3
        self.value = value


    def change(self):
        self.value = 12




ans = []
a = A(13)
ans.append(a.value)
a.change()
ans.append(a.value)
print(ans)

arr = []
arr.append(10)
arr.append(10)
print(11)

cnt = {}
i = 1
if i not in cnt:
    cnt[i] = 1
else:
    cnt[i] += 1

print(cnt)