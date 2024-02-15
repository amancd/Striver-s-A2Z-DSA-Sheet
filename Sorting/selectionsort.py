# [10, 30, 20, 40]
# Assume the first element as minimum and find minimum of the list and swap with the first element, now the first element is sorted, repeat this process.

def SelectionSort(L):
    for i in range(len(L)):
        minimum = i
        for j in range(i+1, len(L)):
            if L[j]<=L[minimum]:
                minimum = j
        L[i], L[minimum] = L[minimum], L[i]
    print(L)
            

def main():
    N = int(input())
    L = []
    for i in range(N):
        item = int(input())
        L.append(item)
    SelectionSort(L)



if __name__ == "__main__":
    main()