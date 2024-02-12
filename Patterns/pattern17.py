#     A
#    ABA
#   ABCBA
#  ABCDCBA

# spaces = 3 2 1
# 1 3 5 7
# keep track of last alphabet and decrement it.


a = "A"
b = 1
d = 1
for i in range(4, 0, -1):
    for k in range(i):
        print(" ", end="")
    for j in range(b):
        print(chr(ord(a)+j), end="")
        c = ord(a)+j
    b = b + 1
    for j in range(d):
        if chr(c-j-1)=="@":
            print(" ", end="")
        else: 
            print(chr(c-j-1), end="")
    d = d + 1
    print("")