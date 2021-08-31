for w in range(35, 36):
    flag = 0
    k = 1
    if w < 10 or w > 99:
        flag = 1
        break
    while w != 85:
        s = 0
        while w != 0:
            c = w % 10
            s += c^2
            w = w // 10
        w = s
        k += 1
        print(w)
        if w < 10 or w > 99:
            flag = 1
            break
    print(w)
    if k == 5 and flag == 0:
        print(w)
        print("cool")

