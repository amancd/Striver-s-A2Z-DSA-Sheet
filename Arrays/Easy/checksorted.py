def checkSorted(arr):
    for i in range(1, len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True



def main():
    arr = [10, 20, 30, 40]
    if checkSorted(arr):
        print("True")
    else:
        print("False")

if __name__ =='__main__':
    main() 