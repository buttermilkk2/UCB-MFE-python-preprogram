'''
1) <2 neighbors dies underpopulation
2) 2 or 3 neighbors lives to next generation
3) >3 neighbors dies overpopulation
4) ==3 neighbors becomes alive
'''

def evolve(initial_state):
    # assume that 1 is alive and 0 is dead
    n = len(initial_state)
    m = len(initial_state[0])

    # short list comprehension for the rows and cols
    tmp_array = [[] * n for _ in range(m)]
    def ev2(rows,cols):
        counter = 0
        points = [(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1)]

        for i,j in points:
            #account for the 0 and 1
            if 0<=rows+j<m and 0<=cols+i<n and initial_state[rows+j][cols+i]==1:
                counter += 1

        # only mind the living cell and count around it
        if board[rows][cols] == 1:
            #underpopulation
            if counter < 2:
                return 0
            #live on
            elif 2<=counter<=3:
                return 1
            #neither
            else:
                return 0
        else: # magical resurrection if there is a group of 3 alive in neighbor cells
            if counter == 3:
                return 1
            else:
                return 0

        #let's iterate for each cells in the rows and cols
        for rows in range(m):
            for cols in range(n):
                tmp_array[rows][cols] = ev2(rows,cols)

        for rows in range(m):
            for cols in range(n):
                initial_state[rows][cols] = tmp_array(rows,cols)

    return initial_state

test_case_1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
]

test_case_2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

test_case_2_next = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


assert evolve(test_case_1) == test_case_1
assert evolve(test_case_2) == test_case_2_next
