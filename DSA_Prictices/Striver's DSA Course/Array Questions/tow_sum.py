## find two elements from an array, where the sum of this two elements are equal to given target value: (var1: return true or false, var2: return the indexes of this elements)

## Brute-force approach:
def brute_twoSum(arr, target):       # TC - O(n^2), SC - O(1)
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return True                    # return i, j 
    return False

## Better approach (using Hashing):           # optimal for ver2
def better_twoSum(arr, target):       # TC - O(n), SC - O(n)
    n = len(arr)
    hash_dict = {}
    for i in range(n):
        rem = target - arr[i]
        if rem in hash_dict:
            return True            # return hash_dict[rem], i
        hash_dict[arr[i]] = i
    return False

## Optimal approach (using Two Pointer and sorting):          # optimal for ver1, not applicable for ver2
def optimal_twoSum(arr, target):             # TC - O(nlogn + n), SC - O(1)
    n = len(arr)
    arr.sort()
    left, right = 0, n-1
    while left < right:
        if arr[left] + arr[right] > target:
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            return True
    return False


arr = [33, 66, 78, 89, 54, 45, 80]
target = 146
result = optimal_twoSum(arr, target)
print(result)