# 1      1
# 12    21
# 123  321
# 12344321

#rows = 4
#spaces = 6, 4, 2, 0
#numbers = reverse

a = 6
for i in range(1, 5):
    for j in range(i):
        print(1+j, end="")
    for k in range(0, a):
        print(" ", end="")
    a = a-2
    for j in range(i, 0, -1):
        print(j, end="")
    print("")
