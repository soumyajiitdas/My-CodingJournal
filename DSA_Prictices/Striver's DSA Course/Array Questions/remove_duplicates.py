## remove duplicate elements from a sorted array and return the size of the array:

## Brute-force approach:
def brute_remove_dupes(arr):       # TC - O(2n), SC - O(n)
    temp = list(set(arr))
    n = len(temp)
    for i in range(n):
        arr[i] = temp[i]
    return n

## Optimal approach
def remove_dupes(arr):             # TC - O(n), SC - O(1)
    n = len(arr)
    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
    return i+1

arr = list(map(int, input("Enter the array: ").split()))
x = remove_dupes(arr)
print(x, arr)