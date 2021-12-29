def func(n):
    n = int(n)
    if (n % 2) == 0:
        return n
    else:
        return 0

answer = []
listik = input().split()
new_listik = map(func, listik)

for i in new_listik:
    if i != 0:
        answer.append(i)
print(answer)
