#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

# rows = 9
# we can combine two patterns

a = 1
for i in range(5, 0, -1):
    for k in range(i):
        print(" ", end="")
    for j in range(a):
        print("*", end="")
    a = a+2
    print("")

a = 9
for i in range(1, 6):
    for k in range(i):
        print(" ", end="")
    for j in range(a):
        print("*", end="")
    a=a-2
    print("")