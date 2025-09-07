## remove duplicate elements from a sorted array and return the size of the array:

## Brute-force approach:
def brute_removeDupes(arr):       # TC - O(2n), SC - O(n)
    temp = set(arr)
    j = 0 
    for i in temp:
        arr[j] = i
        j += 1
    return j

## Optimal approach (for sorted array only):
def removeDupes(arr):             # TC - O(n), SC - O(1)
    n = len(arr)
    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
    return i+1

arr = list(map(int, input("Enter an array: ").split()))
x = brute_removeDupes(arr)
print(x, arr)