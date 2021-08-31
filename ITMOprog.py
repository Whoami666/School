f = open('input.txt', 'r')
F = f.read().split('\n')
n = int(F[0])

weight, number = [], []
plan, t, c = [0]*n, [0]*n, []
count = []
for i in range(1, n+1):
    s = F[i].split()
    weight.append(int(s[0]))
    number.append(int(s[1])-1)
print(number)
a, m = 0, 0
binary = int(n*'1', 2)
for i in range(binary + 1):
    v = bin(i)[2:]
    v = v[::-1]
    for j in range(len(v), n):
        v += '0'
    v = v[::-1]
    print(v)
    m = 0
    for w in range(n):
        if number[w] != int(v[w]):
            m += 1
    if m <= 2:
        for j in range(n):
            a += weight[j]*int(v[j])
        print(number, v, a)
        count.append(a)
    a = 0
for i in range(len(count)):
    c.append(abs(sum(weight) - 2*count[i]))
print(min(c), c)
f = open('output.txt', 'w')
f.write(str((min(c))))
print(weight)