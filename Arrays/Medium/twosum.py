# N = 5, arr[] = {2,6,5,8,11}, target = 14

def fn(arr, target):
    for i in range(len(arr)):
       for j in range(i+1, len(arr)):
          if arr[i] + arr[j] == target:
             return i, j
          
    return False

def main():
   arr = [2, 6, 5, 8, 11]
   print(fn(arr, 14))


if __name__ == "__main__":
   main()