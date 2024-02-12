# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********


a = 0
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    for k in range(0, a):
        print(" ", end="")
    a = a+2
    for j in range(i):
        print("*", end="")
    print("")

b = 8
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    for k in range(0, b):
        print(" ", end="")
    b = b-2
    for j in range(i):
        print("*", end="")
    print("")