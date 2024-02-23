# rotate array by k elements
# [1, 2, 3, 4, 5] by 2 elements at left
# [3, 4, 5, 1, 2]

def fn(arr):
    n = 1
    while n<=2:
        temp = arr[0]
        for i in range(len(arr)):
            if i!= len(arr)-1:
                arr[i] = arr[i+1]
            else:
                arr[i] = temp

        n+=1
        
    print(arr)


def main():
   arr = [1, 2, 3, 4, 5]
   fn(arr)


if __name__ == "__main__":
   main()