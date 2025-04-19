## QUICK SORT of an array:
# when pivot is 1st element:
def p_first(arr, low, high):
    pivot = arr[low]
    i, j = low, high
    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

# when pivot is last element:
def p_last(arr,low,high):
    pivot, i = arr[high], low
    
    for j in range(low, high):
        if arr[j] <= pivot:
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    if i != high:
        arr[i], arr[high] = arr[high], arr[i]
    return i

def qs_first(arr, low, high):
    if low < high:
        pIndex = p_first(arr, low, high)
        qs_first(arr, low, pIndex-1)
        qs_first(arr, pIndex+1, high)

n = int(input())                          # length of the array, example input : 8
arr = list(map(int, input().split()))     # example input : 34 54 23 45 89 55 67 23
qs_first(arr, 0, n-1)
print(' '.join(map(str, arr)))            # output : 23 23 34 45 54 55 67 89