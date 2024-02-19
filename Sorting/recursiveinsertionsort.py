def insertionsort(arr, j, i):
    n = len(arr)
    if i<n:
        j = i
        if j>0 and arr[j-1]>arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j-1

            insertionsort(arr, j-1, 0)
        insertionsort(arr, 0, i+1)


def main():
    arr = [10, 20, 10, 30, 40]
    insertionsort(arr, 0, 0)
    print(arr)


if __name__ == "__main__":
    main()