# Bubble sort works by swapping adjacent elements till the last element is maximum, and the next iteration till maximum index - 1 and so on.

def bubblesort(arr, j, i):
    if j-1>=0:
        if i<j-1:
            if arr[i]>=arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    
            bubblesort(arr, j, i+1)
        bubblesort(arr, j-1, 0)

def main():
    arr = [30, 50, 10, 20]
    bubblesort(arr, len(arr), 0)
    print(arr)

if __name__ == "__main__":
    main()