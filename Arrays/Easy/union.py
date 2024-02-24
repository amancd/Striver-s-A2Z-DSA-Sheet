# Find the union of two arrays
# [1, 2, 3, 4] U [2, 3, 4, 5]
# [1, 2, 3, 4, 5]

def fn(arr1, arr2):
   L = []
   
   for i in range(len(arr1)):
      L.append(arr1[i])

   for j in range(len(arr2)):
      if arr2[j] not in L:
         L.append(arr2[j])

   print(L)

def main():
   arr1 = [1, 2, 3, 4]
   arr2 = [2, 3, 4, 5]
   fn(arr1, arr2)


if __name__ == "__main__":
   main()