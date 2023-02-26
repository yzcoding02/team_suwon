q = []
for i in range(1, 21):
    if i % 3 == 0:
        q.append(i)
q.sort()
q.reverse()
print(q)
