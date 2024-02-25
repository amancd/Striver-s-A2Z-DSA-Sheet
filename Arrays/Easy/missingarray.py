# Find the no missing in the array.
# [1, 2, 3, 4, 6]
# 5

def fn(arr):
    count = 0
    for i in range(len(arr)-1):
       if arr[i+1]-arr[i]!=2:
          print(arr[i]+1)
          count = 1
          break
    
    if count == 0:
       print("No missing elements found!")

def main():
   arr = [1, 2, 3, 4, 5, 6]
   fn(arr)


if __name__ == "__main__":
   main()