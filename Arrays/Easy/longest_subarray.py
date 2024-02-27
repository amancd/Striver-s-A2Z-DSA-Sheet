# Longest subarray with sum k (positive and negative)
# N = 3, k = 1, array[] = {-1, 1, 1}
# 3


def fn(arr, k):
   count = 0
   for i in range(len(arr)):
      sum = 0
      for j in range(i, len(arr)):
         sum+=arr[j]
         if sum==k:
            count = max(count, j-i+1)
    
   print(count)


def main():
   arr = [-1, 1, 1]
   k = 1
   fn(arr, k)


if __name__ == "__main__":
   main()