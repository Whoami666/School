n = 5
s = "abcba"
symbols = {}
words = []
for i in range(n):
    if s[i] in symbols:
        symbols[s[i]] += 1
    else:
        sy = {s[i] : 1}
        symbols.update(sy)

m = n
for i in symbols:
    if symbols[s[i]] < m:
        m = symbols[s[i]]
print(m)
print(symbols)
