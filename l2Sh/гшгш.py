def func(w):
    l = w
    k = 1
    if w < 10 or w > 99:
        return 0
    else:
        while w != 85:
            s = 0
            while w != 0:
                c = w % 10
                s += c * c
                w = w // 10
            w = s
            k += 1
            if w < 10 or w > 99:
                print()
                return 0
        if k == 5:
            return l
        else:
            return 0
cnt = 0
for w in range(10, 100):
    cnt += func(w)
print(cnt)
