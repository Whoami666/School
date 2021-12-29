f = open('input.txt', 'r')
F = f.read().split('\n')
n = int(F[0])
flag = 0
A, B = [], []
for i in range(1, n+1):
    if F[i][2] == '?':
        A.append(F[i])
    else:
        B.append(F[i])
for i in range(len(B)):
    if B.count(B[i]) > 1:
        print("NO")
        flag = 1
if flag == 0:
    k = 10
    for i in range(len(A)):
        A[i] = A[i][0] + str(i % 50) + A[i][3:]

    for i in range(len(A)):
        for j in range(len(A)):
            if j >= i:
                if A[j] == A[i]:
                    A[j] = A[j][0] + str(int(A[1:2]+50)) + A[j][3:]

f = open('output.txt', 'w')
f.write(A)

print(A, B)

