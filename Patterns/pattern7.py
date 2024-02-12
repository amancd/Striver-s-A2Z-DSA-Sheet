#     *
#    ***
#   *****
#  *******
# *********

# rows = 5
# 1 3 5 7 9

a = 1
for i in range(5, 0, -1):
    for k in range(i):
        print(" ", end="")
    for j in range(0, a):
        print("*", end="")
    a = a+2
    print("")
