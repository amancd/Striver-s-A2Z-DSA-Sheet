def frequency(arr):
    mp = {}
    for i in range(len(arr)):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    max_freq = max(mp.values())
    min_freq = min(mp.values())
    
    for key, value in mp.items():
        if value == max_freq:
            print(f"{key} {value}")
        elif value == min_freq:
            print(f"{key} {value}")

def main():
    arr = [10, 5, 10, 15, 10, 5]
    frequency(arr)

if __name__ == "__main__":
    main()