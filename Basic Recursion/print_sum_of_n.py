# Print the sum of first n numbers

def Sum(n, sum):
    if n>=1:
        Sum(n-1, sum + n)
    else:
        print(sum)

def main():
    Sum(5, 0)

if __name__ == "__main__":
    main()