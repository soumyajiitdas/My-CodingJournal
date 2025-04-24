## find the missing number within range 0 to n inclusive which is missing from an array:

## Brute-force approach:

## Better approach (using hashing):

## Optimal approach:
def missingNumber(arr):             # TC - O(n), SC - O(1)
    n = len(arr)

    ## method 1 -- SUM:
    # exp_sum = n*(n+1)//2
    # actual_sum = sum(arr)
    # return exp_sum - actual_sum

    ## method 2 -- XOR (better approach):
    xor1 = xor2 = 0
    for i in range(n):
        xor1 ^= i              # calculates xor from 0 to n-1
        xor2 ^= arr[i]         # calculates xor of every elements in arr
    xor1 ^= n                  # calculates xor of xor1 and n (to get xor from 0 to n)
    return xor1 ^ xor2         # returns the missing num