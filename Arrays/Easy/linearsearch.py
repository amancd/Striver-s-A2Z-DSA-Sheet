# Search an element in an array and return it's index
# [1, 2, 3, 4, 5]
# num = 2
# index = 1

def fn(arr, num):
    for i in range(len(arr)):
       if arr[i] == num:
          print("Element found at index", i)
          break
       elif i==len(arr)-1 and arr[i]!=num:
          print("No element found!")
    

def main():
   arr = [1, 2, 3, 4, 5]
   fn(arr, 5)


if __name__ == "__main__":
   main()