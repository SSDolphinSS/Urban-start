n = int(input())
parol = []
for i in range(1, 21):
    for j in range(2, 21):
        if n % (i + j) == 0:
            if i > j or i == j:
                continue
            else:
                parol.append(i)
                parol.append(j)
print(*parol, sep='')
