# shit the left elment by 1
# [1, 2, 3, 4]
# [2, 3, 4, 1]

def fn(arr):
    temp = arr[0]
    for i in range(len(arr)):
        if i!=len(arr)-1:
            arr[i] = arr[i+1]
        else:
            arr[i] = temp
    
    print(arr)


def main():
   arr = [1, 2]
   fn(arr)


if __name__ == "__main__":
   main()