f = open('input.txt', 'r')
F = f.read().split('\n')
counter = 0
s, s1, s2, s3  = F[0].split(), F[1].split(), F[2].split(), F[3].split()
MinH, SecM = int(s[0]), int(s[1])
HouD, MinD, SecD = int(s1[0]), int(s1[1]), int(s2[2])
h1, m1, s1, h2, m2, s2 = int(s2[0]), int(s2[1]), int(s2[2]), int(s3[0]), int(s3[1]), int(s3[2])
c = int(F[4])

def isit(x, c):
    flag = 0
    if (x == 0 or x % 10 == 0) and c == 0:
        return True
    else:
        while x > 1:
            if x % 10 == c:
                flag = 1
                x //= 10
            else:
                x //= 10
        if flag == 1:
            return True
        else:
            return False
a, b = [], []
a.append(h1)
a.append(m1)
a.append(s1)
b.append(h2)
b.append(m2)
b.append(s2)
print(a, b)
print(isit(a[1], c))
print(a[1], c)
a1, b1 = a.copy(), b.copy()
for i in range(3):
    if isit(a[i], c) == True:

        counter += 1
    if isit(b[i], c) == True:
        counter += 1
sec1, sec2 = h1*MinH*SecM + m1*SecM + s1, h2*MinH*SecM + m2*SecM + s2

for i in range(sec1+1, sec2):
    a1[2] += 1
    if a1[2] == SecM:
        a1[2] = 0
        a1[1] += 1
    if a1[1] == MinH:
        a1[1] = 0
        a1[0] += 1
for i in range(3):
    if isit(a[i], c) == True:
        counter += 1
        print(a1)
        break

print(counter)

print(isit(1234, 3))
f = open('output.txt', 'w')
f.write(str(counter))