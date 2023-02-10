# <숙제>
# 1번
for i in range(1, 11):
    print(i)
# 2번
for i in range(2, 11, 2):
    print(i)
# 3번
for i in range(10, 21):
    if i % 3 != 0:
        print(i)
# 4번
for i in range(50, 101):
    if i % 3 == 0:
        if i % 4 == 0:
            print(i)
# 5번
sum = 0
for i in range(20, 31):
    if i % 5 != 0:
        sum += i
print(sum)
# 6번
sum = 0
mul = 1
for i in range(1, 101):
    if i % 2 == 0:
        mul += i
    if i % 2 == 1:
        sum += i
print(mul - sum)
