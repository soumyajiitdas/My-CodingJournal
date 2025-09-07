## union of two arrays in sorted order:

##Brute-force approach:
def brute_unionOfArray(arr1, arr2):       # TC - O(2m+2n), SC - O(2m+2n)
    temp = set()
    for i in arr1:                   # let size of arr1 = m, tc = O(m) worst case
        temp.add(i)
    for i in arr2:                   # let size of arr2 = n, tc = O(n) worst case
        temp.add(i)                  # sc = O(m+n) -- size of set m+n
    union = list(temp)           # tc = O(m+n), sc = O(m+n) -- this extra space used to returning the answer, not to solve the problem.
    return union

## Optimal approach (array must be sorted):
def unionOfArray(arr1, arr2):                  # TC - O(n1+n2), SC - O(n) -- to returning the answer, not solving the problem.
    n1, n2 = len(arr1), len(arr2)
    i = j = 0
    union_arr = []                              # let the size n
    while n1 > i and n2 > j:
        if arr1[i] <= arr2[j]:
            if len(union_arr) == 0 or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i += 1
        else:
            if len(union_arr) == 0 or union_arr[-1] != arr2[j]:
                union_arr.append(arr2[j])
            j += 1
    while n1 > i:
        if union_arr[-1] != arr1[i]:
            union_arr.append(arr1[i])
        i += 1
    while n2 > j:
        if union_arr[-1] != arr2[j]:
            union_arr.append(arr2[j])
        j += 1
    return union_arr

arr1 = [1, 1, 1, 3, 3, 4 , 5, 7, 9]
arr2 = [0, 1, 2, 2, 5, 6, 7, 7, 8]
print(unionOfArray(arr1, arr2))


