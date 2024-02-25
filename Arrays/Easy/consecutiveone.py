# [1, 1, 0, 1, 1, 1]
# count maximum consecutive 1
# 3

def fn(arr):
    L = []
    count = 0
    for i in range(len(arr)):
       if arr[i]==1:
          count+=1
          if i==len(arr)-1:
             L.append(count)
       else:
          L.append(count)
          count = 0

    print(L)

def main():
   arr = [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1]
   fn(arr)


if __name__ == "__main__":
   main()