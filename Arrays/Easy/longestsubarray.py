# Longest subarray with given sum k(positives)

# N = 3, k = 5, array[] = {2, 3, 5}
# 2

# return largest subarray length

def fn(arr, k):
    count = 0

    for i in range(len(arr)):
       sum = 0
       for j in range(i, len(arr)):
          sum += arr[j]
          if sum == k:
             count = max(count, j-i+1)
    
    print(count)
          


def main():
   arr = [2, 3, 5]
   k = 5
   fn(arr, k)


if __name__ == "__main__":
   main()