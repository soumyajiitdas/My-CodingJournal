## perform a linear search in an array:
def linearSearch(arr, key):
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i
    return -1

arr = list(map(int, input("Enter the array: ").split()))
key = int(input("Enter the key: "))
x = linearSearch(arr, key)
print(x)
