import random


def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def binarysearch(arr, ser, begin, end):

    if begin <= end:
        mid = (begin + end) // 2

        if ser == arr[mid]:
            return mid
        elif ser < arr[mid]:
            return binarysearch(arr, ser, begin, mid-1)
        elif ser > arr[mid]:
            return binarysearch(arr, ser, mid+1, end)
    else:
        return -1


# Get Input
ip = input("Enter the number of Elements : ")

# Form a List
arr = [random.randint(1, 50) for i in range(int(ip))]
print("Unsorted List : ")
print(arr)

bubblesort(arr)
print("Sorted List : ")
print(arr)

# Search an element
ser = input("Enter the element to search : ")
result = binarysearch(arr, int(ser), begin=0, end=len(arr))
print(result)
if result != -1:
    print(f"{ser} is found at {result+1}")
else:
    print("Element is not found!")
