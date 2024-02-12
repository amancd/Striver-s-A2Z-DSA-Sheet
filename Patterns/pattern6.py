# 12345
# 1234
# 123
# 12
# 1

# rows = 5
# cols = reversing order
# 1 is common

for i in range(5, 0, -1):
    for j in range(i):
        print(1+j, end="")
    print("")