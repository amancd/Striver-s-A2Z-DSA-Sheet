# Bubble sort works by swapping adjacent elements till the last element is maximum, and the next iteration till maximum index - 1 and so on.

def bubblesort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if arr[j]>=arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            n = n - 1
    
    print(arr)

def main():
    arr = [30, 50, 10, 20]
    bubblesort(arr)

if __name__ == "__main__":
    main()