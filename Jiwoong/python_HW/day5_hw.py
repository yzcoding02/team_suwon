b = [100, 200, 300, 400]
b.pop()
print(b)
b.pop()
print(b)

c = ["야", "야야", "아니 좀!"]
c.clear()
print(c)

ㅇ = [200, 50, 40, 32]
ㅇ. sort()
print(ㅇ)
e = ["너무 적다", "너무 보통이다", "너무 많다"]
e.sort()
print(e)

f = [299, 499, 1099, 399]
f.reverse()
print(f)
g = ["여기서 200만 줄여", "너무 많아", "너무 적어"]
g.reverse()
print(g)

q = [910, 291, 911, 103]
q.sort()
q.reverse()
print(q)

a = ["정렬 중", "정렬 거의 됨", "복구 실패"]
a.sort()
a.reverse()
print(a)

a = [190, 280, 370]
print(a[-2]*a[-1])

a = [19, 18, 270]
print(a[-2] % a[1])
c = [199, 288, 377, 466, 122]
print(c.count(1))

c = [1980, 2870, 3650, 4540, 100]
print(c.count(5))

e = [1, 2, 3]
e.insert(2, 2.5)
print(e)

i = [1, 2, 3]
i.insert(1, 1.5)
i.insert(2, 2.999)
print(i)

f = [199, 250, 70, 199.99999999999]
f.remove(250)
f.remove(70)
print(f)

g = [99, 88]
h = [19, 28, 37]
g.extend(g)
print(g)

h.extend(h)
print(h)

i = [1, 2.99999999]
j = [3, 3.99999999, 4.9999999]
print(i+j)
print(j+i)

k = [199, 288, 333]
print(len(k))
k.append(453)
print(len(k))

k.clear()
print(len(k))

notfruits = ["not cherry", "but apple", "banananananana"]
for i in range(len(notfruits)):
    print(notfruits[i])

for notfruits in notfruits:
    print(notfruits)
