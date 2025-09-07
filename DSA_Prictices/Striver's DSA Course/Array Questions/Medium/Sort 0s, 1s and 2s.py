# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order. Note: You need to solve this problem without utilizing the built-in sort function.

## Brute-force approach: Using sorting algos. TC - O(n log n), SC- O(n)

## Better approach:
def better_sortingArr(arr):        # TC - O(2n), SC - O(1)
    n = len(arr)
    i = j = k = 0
    for a in range(n):
        if arr[a] == 0:
            i += 1
        elif arr[a] == 1:
            j += 1
        else:
            k += 1
        
    for a in range(i):
        arr[a] = 0
    for a in range(i,i+j):
        arr[a] = 1
    for a in range(i+j, i+j+k):
        arr[a] = 2

## Optimal approach (using Dutch National Flag Algo):          
def sortingArr(arr):         # TC- O(n), SC- O(1)
    n = len(arr)
    low = mid = 0
    high = n-1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

arr = [0, 1, 2, 0, 1, 2]
better_sortingArr(arr)
print(arr)