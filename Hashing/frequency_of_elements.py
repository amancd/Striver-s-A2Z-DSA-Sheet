def hashfn(arr):
    mp = {}
    for i in range(len(arr)):
        if arr[i] in mp:
            mp[arr[i]] +=1
        else:
            mp[arr[i]] = 1
    
    num = int(input())
    return mp[arr[num]]


def main():
    arr = [10, 5, 10, 15, 10, 5]
    print(hashfn(arr))

if __name__ == "__main__":
    main()