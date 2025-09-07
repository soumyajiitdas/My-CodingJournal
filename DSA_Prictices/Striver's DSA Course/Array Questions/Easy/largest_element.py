## find the largest element in an array:

## Brute-force approach:
def brute_largestElement(arr):      # TC - O(nlogn), SC - O(1)
    arr.sort()
    x = arr[-1]
    return x

## Optimal approach:              # TC - O(n) 
def largestElement(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest

arr = list(map(int, input("Enter an array: ").split()))
print (largestElement(arr))