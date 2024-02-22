# use set
# remove the element and shift the element to the left side and while shifting make sure to delete previous element.

def fn(arr):
    n = len(arr)
    i = 0
    while i<n-1:
       if arr[i]==arr[i+1]:
          for j in range(i+1, n-1):
             arr[j] = arr[j+1]
          arr.pop()
          n-=1
       else:
          i+=1

    print(arr)

def main():
   arr = [10, 10, 20, 20, 30, 40]
   fn(arr)


if __name__ == "__main__":
   main()