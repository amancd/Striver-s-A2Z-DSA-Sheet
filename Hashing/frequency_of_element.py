def hashtable(arr):
    arr2 = [0] * max(arr)
    n = len(arr2)
    for i in range(n):
        for j in range(len(arr)):
            if i==arr[j]:
                arr2[i]+=1
    num = int(input("Enter a number: "))
    for j in range(n):
        if j == num:
            return arr2[j]

def main():
    arr = [10, 5, 10, 15, 10, 5]
    print(hashtable(arr))

if __name__ == "__main__":
    main()