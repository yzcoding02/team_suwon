# for i in range(1, 11):
#    print(i)

# for i in range(1, 10):
#    if i % 2 == 0:
#        print(i)

# for i in range(10, 21):
#    if i % 3 != 0:
#        print(i)

# for i in range(49, 100):
#    if i % 3 == 0:
#        if i % 4 == 0:
#            print(i)

# ee = 0
# for i in range(20, 31):
#    if i % 5 != 0:
#        ee += i
# print(ee)

e = 0
a = 0
for i in range(0, 101):
    if i % 2 == 0:
        a += i
    else:
        e += i
    i += 1
print(a-e)
