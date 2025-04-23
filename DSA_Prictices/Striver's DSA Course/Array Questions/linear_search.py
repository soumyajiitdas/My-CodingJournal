## perform a linear search in an array:
def linearSearch(arr, key):     # TC - O(n), SC - O(1)
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i
    return -1

arr = list(map(int, input("Enter an array: ").split()))
key = int(input("Enter a num to search: "))
x = linearSearch(arr, key)
print(x)
