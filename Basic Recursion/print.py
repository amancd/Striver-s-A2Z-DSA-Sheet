# Understand recursion by print

def printf(n):
    if n <= 5:
        print("Hello World!")
        printf(n + 1)

def main():
    printf(1)

if __name__ == "__main__":
    main()
