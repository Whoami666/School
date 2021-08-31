f = open('1902input.txt', 'r')
F = f.read()
F = F.split("\n")
print(F)
lines = F[0].split()
cnt = 0
Y, X = int(lines[0]) + 1, int(lines[1])
for y in range(2, Y):
    for x in range(1, X-1):
        if F[y][x] == "*":
            if(F[y-1][x-1]) == "*" and F[y-1][x+1] == "*":
                cnt += 1
                print(x, y)
for y in range(2, Y):
    if F[y][0] == "*" and F[y-1][1] == "*":
        cnt += 1
        print(X-1, y)
    if F[y][X-1] == "*" and F[y-1][X-2] == "*":
        cnt += 1
        print(X-1, y)
print(cnt)
f = open('output.txt', 'w')