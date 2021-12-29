f = open('input.txt', 'r')
f = f.read().split('\n')
s = f[0].split()
n, M, lencar, lenspace = int(s[0]), int(s[1]), int(s[2]), int(s[3])
space = [0]*M
S = f[1].split()
print(S)
for i in range(n):
    k = int(S[i])
    for j in range(k, k+lencar):
        space[j] = 1
cnt = 0
count = 0
cuunt = 0
cpp = 0
print(space)
for i in range(M):
    if space[i] == 0:
        count += 1
    else:
        count
        break
for i in range(M):
    if space[i] == 0:
        cpp += 1
    else:
        cnt = cpp
        cpp=0
    if cnt - lenspace > count:
        count = cnt
        print(count)
m = space[::-1]
for i in range(M):
    if m[i] == 0:
        cuunt += 1
    else:
        break

f = open('output.txt', 'w')
if (max(count, cuunt) - 2*lenspace) < 1:
    f.write(str(0))
else:
    f.write(str(max(count, cuunt) - 2*lenspace))


