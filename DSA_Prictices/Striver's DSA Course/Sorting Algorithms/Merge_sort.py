## MARGE SORT of an array:
def merge(arr, low, mid, high):
    temp = []
    left, right = low, mid+1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1

    arr[low:high+1] = temp


def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low , mid, high)


n = int(input())                          # length of the array, example input : 8
arr = list(map(int, input().split()))     # example input : 34 54 23 45 89 55 67 23
merge_sort(arr, 0, n-1)
print(' '.join(map(str, arr)))            # output : 23 23 34 45 54 55 67 89