# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

# rows = 5
# numbers are alternative
# right triangle pattern


for i in range(1, 6):
    for j in range(i):
        print((i+j)%2, end="")
    print("")
    