## SELECTION SORT of an array:
def selection_sort(arr, n):
    for i in range(n-1):             #sort will perform till 0 to (n-2)th index
        mini = i
        for j in range(i, n):            #search for minimum value in range i to last i.e. (n-1)th index
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]     #swap current arr[i] with minimum value   

n = int(input())                          # length of the array, example input : 8
arr = list(map(int, input().split()))     # example input : 34 54 23 45 89 55 67 23
selection_sort(arr, n)
print(' '.join(map(str, arr)))            # output : 23 23 34 45 54 55 67 89