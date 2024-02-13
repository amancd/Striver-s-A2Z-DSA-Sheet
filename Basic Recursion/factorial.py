# Factorial using recursion

def factorial(fact, n):
    if n>=1:
        factorial(fact * n, n-1)
    else:
        print(fact)
    
def main():
    factorial(1, 5)

if __name__ == "__main__":
    main()