# check if a string is palindrome

def palindrome(str1, i, n):
    if i<=n:
        if str1[n-1] == str1[i]:
            palindrome(str1, i+1, n-1)
        else:
            print("Not a palindrome")
    else:
        print("Palindrome")

    

def main():
    str1 = "ABA"
    palindrome(str1, 0, len(str1))

if __name__ == "__main__":
    main()