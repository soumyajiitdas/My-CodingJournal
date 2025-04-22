## check if the array is sorted or not:
def isSorted(arr):          # TC - O(n), SC - O(1)
    n = len(arr) 
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
        else:
            pass
    return True

arr = (map(int, input("Enter the array: ").split()))
# a1 = [27, 47, 57, 65, 43, 58, 68]
# a2 = [45, 55, 67, 76, 78, 88, 89, 90, 99]
print(isSorted(arr))