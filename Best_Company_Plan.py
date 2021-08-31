f = open('input.txt', 'r')
F = f.read().split('\n')
N = F[0].split()
T, n = int(N[0]), int(N[1])
time, money = [], []
plan, t, c = [0]*n, [0]*n, [0]*n
count = []
for i in range(1, n+1):
    s = F[i].split()
    time.append(int(s[0]))
    money.append(int(s[1]))
print(time, money)
binar = int(('1'*n), 2)
for i in range(binar+1):
    v = bin(i)[2:]
    v = v[::-1]
    for k in range(len(v)):
        plan[k] = int(v[k])
    for k in range(len(v), n):
        plan[k] = 0
    print(plan)
    for l in range(n):
        t[l] = plan[l]*time[l]
        c[l] = plan[l]*money[l]
    print(t, c)
    if sum(t) <= T:
        count.append(sum(c))
print((max(count)), count)
f = open('output.txt', 'w')
f.write(str(max(count)))


