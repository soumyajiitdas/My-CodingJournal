if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    lowest, sec_lowest = float('inf'), float('inf')
    for i in records:
        if i[1] < lowest:
            sec_lowest = lowest
            lowest = i[1]
        elif i[1] > lowest and i[1] < sec_lowest:
            sec_lowest = i[1]
    
    result = []
    for j in records:
        if j[1] == sec_lowest:
            result.append(j[0])
            
    for name in sorted(result):
        print(name)