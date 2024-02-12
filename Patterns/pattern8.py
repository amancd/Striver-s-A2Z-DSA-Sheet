# *********
#  *******
#   *****
#    ***
#     *

#rows = 5
#cols = reversing order
#space = 0, 1, 2, 3, 4
#star = 9, 7, 5, 3, 1

a = 9
for i in range(1, 6):
    for k in range(i):
        print(" ", end="")
    for j in range(0, a):
        print("*", end="")
    a=a-2
    print("")