# E
# DE
# CDE
# BCDE
# ABCDE

a = "G"
for i in range(1, 6):
    for j in range(i+1, 1, -1):
        print(chr (ord(a)-j), end="")
    print("")