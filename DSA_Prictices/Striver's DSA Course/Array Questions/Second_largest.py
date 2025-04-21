## find the second largest element in an array:

## Brute-force approach:
def brute_second_largest(arr):
    arr.sort()
    large_el = arr[-1]
    sec_large_el = arr[0]
    for i in arr:
        if i != large_el:
            sec_large_el = i
    return sec_large_el

## Better approach:
def better_second_largest(arr):
    large = sec_large = float('-inf')
    for i in arr:
        if i > large:
            large = i
    for j in arr:
        if large > j > sec_large:
            sec_large = j
    return sec_large

## Optimal approach:
def second_largest(arr):
    largest_element = second_largest_element = float('-inf')
    for i in arr:
        if i > largest_element:
            second_largest_element = largest_element
            largest_element = i
        elif largest_element > i > second_largest_element:
            second_largest_element = i
    return second_largest_element


arr = list(map(int, input("Enter the array: ").split()))
# array = [28,48,58,63,26,68]
print (second_largest(arr))