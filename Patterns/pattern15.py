# ABCDE
# ABCD
# ABC
# AB
# A

a = "A"
for i in range(5, 0, -1):
    for j in range(i):
        print(chr(ord(a) + j), end="")
    print("")