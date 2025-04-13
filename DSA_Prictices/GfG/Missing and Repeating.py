#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n = len(arr)
        hash_dict = {}
        a, b = -1, -1
        
        for i in arr:
            if i in hash_dict:
                a = i
                break
            hash_dict[i] = 1
        
        expected_sum = n*(n+1)//2
        actual_sum = sum(arr)
        b = expected_sum - (actual_sum - a)
        
        return [a,b]



#{ 
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends