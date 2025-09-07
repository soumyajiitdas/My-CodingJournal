## find the second largest element in an array:

## Brute-force approach:
def brute_secondLargest(arr):    # TC - O(n+nlogn), SC - O(1)
    arr.sort()
    largest = arr[-1]
    sec_largest = arr[0]
    for i in arr:
        if i != largest:
            sec_largest = i
    return sec_largest

## Better approach:
def better_secondLargest(arr):                    # TC - O(2n)
    largest = secLargest = float('-inf')
    for i in arr:
        if i > largest:
            largest = i
    for j in arr:
        if largest > j > secLargest:
            secLargest = j
    return secLargest

## Optimal approach:
def second_largest(arr):                                              # TC - O(n)
    largest_element = second_largest_element = float('-inf')
    for i in arr:
        if i > largest_element:
            second_largest_element = largest_element
            largest_element = i
        elif largest_element > i > second_largest_element:
            second_largest_element = i
    return second_largest_element


arr = list(map(int, input("Enter an array: ").split()))
# array = [28,48,58,63,26,68]
print (second_largest(arr))