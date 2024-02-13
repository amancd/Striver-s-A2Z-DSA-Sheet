# print n to 1 by recursion

def printf(n):
    if n>=1:
        print(n)
        printf(n-1)

def main():
    printf(10)

if __name__ == "__main__":
    main()