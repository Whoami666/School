f = open('input.txt', 'r')
f = f.read().split('\n')
n = int(f[0])
weights = []
numbers = []
total = 0
for i in range(1, n + 1):
    x = f[i].split()
    weights.append(int(x[0]))
    total += int(x[0])
    if(x[1] == '2'):
        numbers.append(1)
    else:
        numbers.append((-1))
counter = 10000000
new = [0] * n
print(total)
new = numbers
cup = 0
for i in range(n):
    cup += new[i] * weights[i]
counter1 = abs(cup)
print(new, counter1)

for b in range(n):
    new = numbers
    new[b] = new[b]*(-1)

    cup = 0
    for i in range(n):
        cup += new[i]*weights[i]
    counter1 = abs(cup)
    print(new, counter1)
    if counter1 < counter:
        counter = counter1
        z = new

for a in range(n):
    for b in range(n):
        new = numbers
        new[a] = new[a]*(-1)
        new[b] = new[b]*(-1)

        cup = 0
        for i in range(n):
            cup += new[i]*weights[i]
        counter1 = abs(cup)
        print(new, counter1)
        if counter1 < counter:
            counter = counter1
            z = new
f = open('output.txt', 'w')
f.write(str(counter))









