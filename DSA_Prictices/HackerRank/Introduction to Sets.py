def average(array):
    # your code goes here
    array_set = set(arr)
    sum = 0
    for i in array_set:
        sum += i
    avg = sum/len(array_set)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)