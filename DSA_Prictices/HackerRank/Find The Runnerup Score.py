if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner_score, runner_up_score = float('-inf'), float('-inf')   # negative infinity

    ##brute force, sort arr and use for loop TC, SC = O(n+nlogn), O(1)

    ##better approach; TC, WC = O(2n), O(1) [without the map function]:
    # for i in arr:
    #     if i > winner_score:
    #         winner_score = i
    # for j in arr:
    #     if winner_score > j > runner_up_score:
    #         runner_up_score = j


    ## Optimal Solution, TC, SC = O(n), O(1):
    for j in arr:
        if j > winner_score:
            runner_up_score = winner_score
            winner_score = j
        elif winner_score > j > runner_up_score:
            runner_up_score = j


    print(runner_up_score)



