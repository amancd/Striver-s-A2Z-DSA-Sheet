# num = 5
# num is only divisble by 5 and 1
# prime numbers

num = 5
count = 0
for i in range(1, num+1):
    if num%i==0:
        count = count + 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")