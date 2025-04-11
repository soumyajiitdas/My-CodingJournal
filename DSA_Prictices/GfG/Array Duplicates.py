class Solution:
    def findDuplicates(self, arr):
        # code here
        hash_arr = [0 for i in range(max(arr)+1)]
        for j in arr:
            hash_arr[j] += 1
        return [k for k in range(len(hash_arr)) if hash_arr[k]>1]
        



#{ 
# Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().findDuplicates(arr)  # find the duplicates
    # Sort the result in ascending order
    s.sort()
    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print duplicates in ascending order
    else:
        print("[]")  # Print empty list if no duplicates are found
    print("~")

# } Driver Code Ends