# ****
# *  *
# *  *
# ****

a = 0
for i in range(2, 0, -1):
    for j in range(i):
        print("*", end="")
    for k in range(a):
        print(" ", end="")
    a = 2
    for j in range(i):
        print("*", end="")
    print("")

b = 2
for i in range(1, 3):
    for j in range(i):
        print("*", end="")
    for k in range(b):
        print(" ", end="")
    b = 0
    for j in range(i):
        print("*", end="")
    print("")