# 1
# for i in range(7):
#     print("내일은 토요일이다")
# 2
# for i in range(3, 11, 3):
#     print(i)
# 4
# for i in range(50, 101):
#     if i % 3 == 0:
#         if i % 4 == 0:
#             print(i)
# 5
# sum = 0
# mul = 1
# for i in range(1, 101):
#     if i % 2 == 0:
#         mul += i
#     if i % 2 == 1:
#         sum += i
# print(mul - sum)
# 3
sum = 0
for i in range(1, 21):
    if i % 4 != 0:
        sum += i
print(sum)