## move all zeros to the end of the array:

## brute-force approach;
def brute_move_zeros(arr):
    temp = []
    for i in arr:
        if i != 0:
            temp.append(i)

    temp_size = len(temp)
    for i in range(temp_size):
        arr[i] = temp[i]

    n = len(arr)
    for i in range(temp_size, n):
        arr[i] = 0

## Optimal approach:
def move_zeros(arr):
    n = len(arr)
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break    
    for i in range(j+1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

arr = list(map(int, input("Enter the array: ").split()))
move_zeros(arr)
print(arr)