# A
# BB
# CCC
# DDDD
# EEEEE

a = "A"
for i in range(0, 5):
    for j in range(i+1):
        print(chr(ord(a)+i), end="")
    print("")