# A
# AB
# ABC
# ABCD
# ABCDE

a = "A"
for i in range(1, 6):
    for j in range(i):
        print(chr(ord(a) + j), end="")
    print("")