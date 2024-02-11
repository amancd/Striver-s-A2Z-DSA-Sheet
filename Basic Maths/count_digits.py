#num = 123
#digits = 3

#123//10 = 12
#123%10 = 3


num = 123
count = 0
while(num!=0):
    num = num//10
    count = count + 1

print(count)