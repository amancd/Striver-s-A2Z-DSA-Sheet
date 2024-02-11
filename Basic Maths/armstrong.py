#num = 153
#digit = 3
#num = 1^3 + 5^3 + 3^3 = 153
#armstrong = true

#first find out digits in the number
#use the digits to calculate their sum

num = 170
n = num
count = 0
temp = 0
arm = num

while(n!=0):
    n = n//10
    count = count + 1

while (arm!=0):
    temp = pow((arm%10),count) + temp
    arm = arm//10

if temp == num:
    print("Armstrong number")
else:
    print("Not an armstrong")