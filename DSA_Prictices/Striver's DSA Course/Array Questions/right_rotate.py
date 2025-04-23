## right rotate (last comes to first) an array by d places:

## Brute-force approach:
def brute_rightRotate(arr, d):       # TC - O(n+d), SC - O(d)
    n = len(arr)
    if  n < d:
        d = d % n
    if d != n or d > 0:
        temp = arr[n-d:]

        for i in range(n-1, d-1, -1):
            arr[i] = arr[i-d]

        for i in range(d):
            arr[i] = temp[i]

def rightRotate(arr, d):                # TC - O(2n), SC - O(1)
    n = len(arr)
    if  n < d:
        d = d % n
    if d != n or d > 0:
        arr[:d+1] = arr[:d+1][::-1]
        arr[d+1:] = arr[d+1:][::-1]
        arr[:] = arr[:][::-1]

arr = list(map(int, input("Enter an array: ").split()))
d = int(input("Enter a num to rotate: "))
rightRotate(arr, 3)
print(arr)