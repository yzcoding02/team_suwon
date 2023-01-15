for i in range(3, 11, 3):  # =1~10중에 3배수 2번번
    print(i)

sum = 0  # =1~20 4배수 아닌수
for i in range(1, 21, 1):
    if i % 4 != 0:
        sum += i

print(sum)

for i in range(50, 101): #50~100까지 3,4 공배수
    if i % 3 == 0:
        if i % 4 == 0:
            print(i)

sum = 0
mul = 1
for i in range(1, 101): #1~100까지수중 짝수의 합-홀수의 합
    if i % 2 == 0:
        mul += i
    if i % 2 == 1:
        sum += i
print(mul - sum)