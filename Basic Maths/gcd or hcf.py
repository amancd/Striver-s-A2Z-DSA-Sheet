# num1 = 10
# num2 = 5

# gcd = 5 because it divides both numbers

# if num1>num2 then it cannot divides num2
# if num1%num2 == 0 then num2 is gcd
# else if num2 can't divide num1 then we need to iterate backwards from num2 till 1 and if we found any number which divides both of them break

num1 = 10
num2 = 5

num = num1

if num1>num2:
    if num1%num2==0:
        print(num2)
else:
    if num2%num1==0:
        print(num1)
    else:
        while(num>1):
            if num1%num==0 and num2%num==0:
                print(num)
                break;
            num = num - 1