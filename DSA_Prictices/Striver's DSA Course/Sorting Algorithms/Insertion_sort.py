## INSERTION SORT of an array:
def insertion_sort(arr, n):
    for i in range(n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

## Recursive INSERTION SORT:
def recursive_is(arr, n, i=0):
    if i == n:
        return
    j = i
    while j > 0 and arr[j-1] < arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1
    
    recursive_is(arr, n, i+1)


n = int(input())                          # length of the array, example input : 8
arr = list(map(int, input().split()))     # example input : 34 54 23 45 89 55 67 23
insertion_sort(arr, n)
# recursive_is(arr, n)
print(' '.join(map(str, arr)))            # output : 23 23 34 45 54 55 67 89