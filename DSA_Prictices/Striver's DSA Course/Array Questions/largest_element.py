## find the largest element in an array:

## Brute-force approach:
def brute_largest_element(arr):      # TC - O(nlogn), SC - O(1)
    arr.sort()
    x = arr[-1]
    return x

## Optimal approach:              # TC - O(n) 
def largest_element(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest

arr = list(map(int, input("Enter the array: ").split()))
print (largest_element(arr))