def insertionsort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j-1

    print(arr)


def main():
    arr = [10, 20, 10, 30, 40]
    insertionsort(arr)


if __name__ == "__main__":
    main()