# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

a=1
for i in range(1, 6):
    for j in range(i):
        print(a, end="")
        a = a + 1
    print("")