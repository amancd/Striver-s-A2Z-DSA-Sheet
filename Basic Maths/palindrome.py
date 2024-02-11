#num = 121
#palindrome = true

#if rev == num return true

num = 121
n = num
rev = 0
while(n!=0):
    rev = rev*10 + n%10
    n = n//10

if rev == num:
    print("Yes it is a palindrome")
else:
    print("No it is not a palindrome")