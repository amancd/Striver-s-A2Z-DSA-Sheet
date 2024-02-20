def largest(arr):
    maximum = arr[0]
    for i in range(1, len(arr)):
        if maximum <= arr[i]:
            maximum = arr[i]
    
    return maximum

def main():
    arr = [10, 20, 30, 40, 50]
    print(largest(arr))

if __name__ == "__main__":
    main()