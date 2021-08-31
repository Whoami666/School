f = open('painful.txt', 'r')
F = f.read()
F = F.split("\n")
cnt = 0
F0, F1, F2, F3 = F[0].split(), F[1].split(), F[2].split(), F[3].split()
A = int(F0[0])
B = int(F0[1])
X, Y, Z = int(F1[0]), int(F1[1]), int(F1[2])
H1, M1, S1 = int(F2[0]), int(F2[1]), int(F2[2])
sec1 = H1*A*B + M1*B + S1
H2, M2, S2 = int(F3[0]), int(F3[1]), int(F3[2])
sec2 = H2*A*B + M2*B + S2
c = int(F[4])
clock = [0, 0, 0]
print(sec1, sec2)
for sec in range(sec1, sec2+1):
        clock[0] = sec // (A*B)
        clock[1] = (sec - clock[0]) // B
        clock[2] = sec - clock[0] - clock[1]
        if clock.count(c) > 0:
            cnt += 1
f = open('output.txt', 'w')
f.write(str(cnt))
print(cnt)
f.close()









