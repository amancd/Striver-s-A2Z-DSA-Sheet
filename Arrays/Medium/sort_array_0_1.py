# Input: nums = [2,0,2,1,1,0]
# [0,0,1,1,2,2]

def fn(nums):
    n = len(nums)
    for i in range(n-1, 0, -1):
       for j in range(0, i):
          if nums[j]>=nums[i]:
             nums[i], nums[j] = nums[j], nums[i]
    print(nums)


def main():
   nums = [2, 0, 2, 1, 1, 0]
   fn(nums)


if __name__ == "__main__":
   main()