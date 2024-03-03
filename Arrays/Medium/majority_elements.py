# N = 3, nums[] = {2,2,1,1,1,2,2}

def fn(nums, n):
   b = n//2
   counter = 1
   for i in range(n):
      counter = 1
      for j in range(i+1, n):
         if nums[i]==nums[j]:
            counter+=1
      if counter>=b:
         return nums[i]
    
   return -1


def main():
   nums = [1, 1, 1, 2, 2, 2, 2]
   print(fn(nums, len(nums)))


if __name__ == "__main__":
   main()