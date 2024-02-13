# print 1 to n times using recursion

def printf(i, n):
    if i<=n:
        print(i)
        printf(i+1, n)

def main():
    printf(1, 10)

if __name__ == "__main__":
    main()