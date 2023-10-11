def valid_sudoku(board):
        placement_map = {i:[] for i in range(29)}
       
        baseSection = 17
        for rowHeader, row in enumerate(board, 9):
            for columnHeader, value in enumerate(row):
                currentSection = baseSection + (columnHeader // 3)
                print(rowHeader, currentSection, columnHeader)
                if value != ".":
                    if (value in placement_map[columnHeader]) or (value in placement_map[rowHeader]) or (value in placement_map[currentSection])  :
                        print("Failed")
                        
                    placement_map[rowHeader].append(value)
                    placement_map[columnHeader].append(value)
                    placement_map[currentSection].append(value)
            if((rowHeader+2) % 3 == 0):
                baseSection += 3


        return True         



test1 =[
    ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
    ]

test2 =[
    ["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
    ]

valid_sudoku(test1)

