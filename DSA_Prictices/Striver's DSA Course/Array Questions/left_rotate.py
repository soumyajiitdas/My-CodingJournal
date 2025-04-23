## left rotate (first goes to last) an array by d places:

## Brute-force approach:
def brute_left_rotate(arr, d):       # TC - O(n+d), SC - O(d)
    n = len(arr)
    if  n < d:
        d = d % n

    if d != n or d > 0:
        temp = arr[:d]
        for i in range(d, n):
            arr[i-d] = arr[i]

        for i in range(n-d, n):
            arr[i] = temp[i-(n-d)]

## Optimal approach:
def left_rotate(arr, d):             # TC - O(2n), SC - O(1)
    n = len(arr)
    if  n < d:
        d = d % n
    if d != n or d > 0:
        arr[:d] = arr[:d][::-1]
        arr[d:] = arr[d:][::-1]
        arr[:] = arr[:][::-1]

arr = list(map(int, input("Enter an array: ").split()))
d = int(input("Enter a num to rotate: "))
left_rotate(arr, 3)
print(arr)
