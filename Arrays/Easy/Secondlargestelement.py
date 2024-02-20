def largest(arr):
    maximum = float('-inf')
    secondmax = float('-inf')
    for i in range(len(arr)):
        if maximum <= arr[i]:
            maximum = arr[i]
    
    for i in range(len(arr)):
        if secondmax <= arr[i] and arr[i]!=maximum:
            secondmax = arr[i]
        
    return secondmax

def secondsmallest(arr):
    minimum = float('inf')
    secondmin = float('inf')
    for i in range(len(arr)):
        if minimum >= arr[i]:
            minimum = arr[i]
    
    for i in range(len(arr)):
        if secondmin >= arr[i] and arr[i]!=minimum:
            secondmin = arr[i]
        
    return secondmin


def main():
    arr = [50, 40, 20, 10, 30]
    print("Second Largest: ",largest(arr))
    print("Second Smallest: ",secondsmallest(arr))

if __name__ == "__main__":
    main()