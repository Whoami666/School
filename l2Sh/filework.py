f = open('dataset_3380_5.txt')
f1 = open('answer.txt', 'w')
s = f.readline().split()
print(s)
dic = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': []}
while len(s) > 0:
    dic[s[0]].append(int(s[2]))
    s = f.readline()
    if len(s) > 0:
        s = s.split()
for d in dic:
    if len(dic[d]) == 0:
        print(d, "-")
        answ = str(d) + " -"
    else:
        print(d, sum(dic[d])/len(dic[d]))
        answ = str(d) + " " + str(sum(dic[d])/len(dic[d]))
    f1.write(answ + '\n')
f.close()
f1.close()
