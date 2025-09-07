## find the longest sub array within a given array where the sum of the elements of the sub array is K and return the max length:

## Brute-force approach:
def brute_longestSubArray(arr, k):                 # TC - O(n^2), SC - O(1)
    n = len(arr)
    max_len = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum == k:
                max_len = max(max_len, j-i+1)
    return max_len

## Better approach (using Hashing) (optimal for arrays which contains negatives):
def better_longestSubArray(arr, k):                 # TC - O(n), SC - O(n)
    n = len(arr)
    hash_dict = {}
    sum = max_len = 0 
    for i in range(n):
        sum += arr[i]
        if sum == k:
            max_len = max(max_len, i+1)
        rem = sum - k
        if rem in hash_dict:
            length = i - hash_dict[rem]
            max_len = max(max_len, length)
        if sum not in hash_dict:
            hash_dict[sum] = i
    return max_len

## Optimal approach (using Two Pointer) (optimal for arrays which contains only 0s and Positives):
def longestSubArray(arr, k):                       # TC - O(n), SC - O(1)
    n = len(arr)
    left = right = 0
    sum = 0
    maxLen = 0
    while right < n:
        sum += arr[right]
        while left <= right and sum > k:
            sum -= arr[left]
            left += 1
        if sum == k:
            maxLen = max(maxLen, (right-left)+1)
        right += 1
    return maxLen


arr = list(map(int, input("Enter an array: ").split()))
k = int(input("Enter k: "))
# a = [2, 3, 5, 1, 1, 1, 4, 2, 1, 9]   # s = 10
# b = [2, 0, -2, 0, 0, 0, 3]           # s = 3
# s = 10
result = longestSubArray(arr, k)
print(result)