Z = []
for i in range(1, 21):
    if i % 3 == 0:
        Z.append(i)
Z.sort()
Z.reverse()
print(Z)
