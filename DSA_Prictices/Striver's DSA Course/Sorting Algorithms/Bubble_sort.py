## BUBBLE SORT of an array:
# Brute-force approach:
def brute_bs(arr, n):
    for i in range(n-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Optimal approach:
def bubble_sort(arr, n):
    didSwap = 0                                       # set a swap tracker
    for i in range(n-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:                      # checks if adjacent elements are sorted order
                arr[j], arr[j+1] = arr[j+1], arr[j]    # if no then swap
                didSwap = 1
        if didSwap == 0:                               # Optimization: if no swaps => array sorted
            break

## Recursive BUBBLE SORT algorithm:
def recursive_bs(arr, n):
    if n == 1:                                       # base case
        return
    didSwap = 0
    for j in range(n-1):                             # inner loop
        if arr[j] > arr[j+1]:     
            arr[j], arr[j+1] = arr[j+1], arr[j]
            didSwap = 1                              # track swaps
    if didSwap == 0:
        return
    recursive_bs(arr, n-1)


n = int(input())                          # length of the array, example input : 8
arr = list(map(int, input().split()))     # example input : 34 54 23 45 89 55 67 23
bubble_sort(arr, n)
# recursive_bs(arr, n)
print(' '.join(map(str, arr)))            # output : 23 23 34 45 54 55 67 89
