f = open('input.txt', 'r')
F = f.read().split('\n')
n = int(F[0])
k = 10
A = [0]*n
for i in range(1, n+1):
    A[i-1] = F[i

for i in range(n):
    if A[i][1] != '?' and F.count(A[i]) > 1:
        print("NO")
        flag = 1
    else:
        B = A
        C = []
        k = 0
        z = A[i]
        while(A.count(z) > 0):
            C.append(A.index(A[i])+k)
            A.pop(A.index(A[i]))
            k+=1
        A = B
        d = 10
        for i in range(len(C)):
            A[C[i]] = d
            d += 1
for i in range(len(A)):
    print(A[i])