# Move zeroes to the end
# [1, 0, 2, 0, 0, 0, 3, 4, 0]
# [1, 2, 3, 4, 0, 0, 0, 0, 0]

def fn(arr):
    for i in range(len(arr)-1):
       if arr[i]==0:
          for j in range(i, len(arr)-1):
             if arr[j]!=0:
                arr[i], arr[j] = arr[j], arr[i]
                break
    
    print(arr)


def main():
   arr = [1, 0, 2, 0, 0, 0, 3, 4, 0]
   fn(arr)


if __name__ == "__main__":
   main()