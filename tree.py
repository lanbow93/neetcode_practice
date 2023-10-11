def tree(h, q):
    solution_list = []
    for num in q:
        if(num == (2^h)-1):
            solution_list.append(-1)
        elif(num % 2 == 0):
            solution_list.append(num * 2)
        elif(num % 2 != 0):
            solution_list.append((num * 2) +1)
    print(solution_list)

tree(5, [19,14,28])