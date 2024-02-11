# num = 36

# 36 times iteration that is not good

# Optimal Solution
# a * a = n
# a = sqrt n
# a * b < = n
# b = n//a

num = 36

for i in range(1, int(num**0.5)+1):
    if num%i==0:
        print(i)
        if (i!=num//i):
            print(num//i)
