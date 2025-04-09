if __name__ == '__main__':
    N = int(input())
    list = []
    
    for _ in range(N):
        command = input().split()
        operation = command[0]
        
        if operation == "insert":
            list.insert(int(command[1]), int(command[2]))
        elif operation == "print":
            print(list)
        elif operation == "remove":
            list.remove(int(command[1]))
        elif operation == "append":
            list.append(int(command[1]))
        elif operation == "sort":
            list.sort()
        elif operation == "pop":
            list.pop()
        elif operation == "reverse":
            list.reverse()