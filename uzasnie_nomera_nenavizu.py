f = open('input.txt', 'r')
F = f.read().split('\n')
n = int(F[0])
coffee_destruction, normal_dict = [], {}
for i in range(1, n+1):
    coffee_destruction.append(F[i])
transient, transient1 = [], []
for i in range(1, n+1):
        normal_dict[i] = F[i]
f = open('output.txt', 'w')
for i in range(n):
    if coffee_destruction[i][1] != '?' and coffee_destruction.count(coffee_destruction[i]) > 1:
        f.write("NO")
else:
    f.write("YES")
    for i in range(len(coffee_destruction)):
            if coffee_destruction[i][1] == '?' and coffee_destruction[i] != 'empty':
                s = coffee_destruction[i]
                transient.append(i)
                for j in range(i+1, len(coffee_destruction)):
                    if s == coffee_destruction[j]:
                        transient.append(j)
                        coffee_destruction[j] = 'empty'
                for l in range(len(transient)):
                    transient1.append(s[0] + str(l+10) + s[3:])
                for m in range(len(transient)):
                    normal_dict[transient[m]+1] = transient1[m]
                transient, transient1 = [], []
    for i in range(n):
        print(normal_dict[i+1])
for i in range(n):
    f.write('\n')
    f.write(normal_dict[i + 1])
