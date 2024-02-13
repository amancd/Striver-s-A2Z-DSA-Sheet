# reverse a given array using recursion

def reverse(arr2, arr, n, i):
    if n>=0 and i<len(arr):
        arr2[n-1] = arr[i]
        reverse(arr2, arr, n-1, i+1)
    else:
        print(arr2)

def main():
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    reverse([0] * n, arr, n, 0)

if __name__ == "__main__":
    main()

