## calculate maximum consecutive ones from an array which contains 0s and 1s:
def maxConsecutiveOnes(arr):
    count = max_counts = 0
    for i in arr:
        if i == 1:
            count += 1
            max_counts = max(max_counts, count)
        else:
            count = 0
    return max_counts

arr = list(map(int, input("Enter an array which contains binary digits: ").split()))
result = maxConsecutiveOnes(arr)
print(result)