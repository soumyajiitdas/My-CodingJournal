## Brute force - using loop in the loop, TC - O(N*N)
## Better solution: (using Hashing)
def better_majorityElement(arr):      # TC - O(2N), SC - O(N)
    n = len(arr)
    hash_dict = {}
    for el in arr:
        if el in hash_dict:
            hash_dict[el] += 1
        else:
            hash_dict[el] = 1
      
    for key in hash_dict:
        if hash_dict[key] > n//2:
            return key
        
    return -1

## Optimal solution TC - O(2N), SC - O(1)
def majorityElement(nums):             # using Boyer-Moore Majority Vote algorithm
    n = len(nums)
    cnt = el = 0
    for i in range(n):
        if cnt == 0:
            el = nums[i]
            cnt = 1
        elif nums[i] == el:
            cnt += 1
        else: 
            cnt -= 1

    val = 0
    if cnt > 0:
        for i in range(n):
            if nums[i] == el:
                val += 1
    
    if val > n//2:
        return el

    return -1


arr = [2, 4, 5, 2, 2, 4, 9, 5, 4, 4, 7, 8, 5, 5]
print(majorityElement(arr))
