if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner_score, runner_up_score = -1, -1
    for j in range(n):
        if arr[j] > winner_score:
            runner_up_score = winner_score
            winner_score = arr[j]
        elif arr[j] < winner_score and arr[j] > runner_up_score:
            runner_up_score = arr[j]

    print(runner_up_score)



