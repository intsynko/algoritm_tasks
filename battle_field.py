'''
You are in a battlefield which is represented by an integer matrix. For now, each cell can be a mine (denoted by -1) or a safe space (0).

field = [
  [0,  0,  0, -1, -1],
  [0,  0, -1,  0, -1],
  [0, -1,  0, -1,  0],
  [0,  0, -1,  0, -1],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
]

The person can move 1 space at a time up, down, left, or right. The person can't go through mine or land on a mine, or go through the edges of the field.

Given a field and an end position for the person, write a function to determine if it is possible to travel from every safe spot in the field to the given end position.

field1 = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0, -1 ],
    [ 0,  0,  0, 0,  0 ],
]

field2 = [
    [  0,  0,  0, 0, -1 ],
    [  0, -1, -1, 0,  0 ],
    [  0,  0,  0, 0,  0 ],
    [ -1, -1,  0, 0,  0 ],
    [  0, -1,  0,-1,  0 ],
    [  0, -1,  0, 0,  0 ],
]

field3 = [
    [ 0,  0,  0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0,  0,  0, 0 ],
]

field4 = [
    [0,  0,  0,  0, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0,  0,  0,  0, 0],
]

field5 = [
    [0],
]

end = (x,y) # x represents the row and y represents the column, zero based indexing

end1 = (0, 0) # Top left corner
end2 = (5, 0) # For field1, (5,0) represents the bottom left corner 

Expected output:

isReachable(field1, end1) -> True
isReachable(field1, end2) -> True
isReachable(field2, end1) -> False
isReachable(field2, end2) -> False
isReachable(field3, end1) -> False
isReachable(field4, end1) -> True
isReachable(field5, end1) -> True


n: width of the input field
m: height of the input field
'''

def free_walker(matrix: list, position: tuple, visited: set):
    i, j = position
    visited.add((i,j))

    def check_(next_pos):
        i_, j_ = next_pos
        return i_ < len(matrix) and j_ < len(matrix[i_]) and i_ >= 0 and j_ >= 0 \ 
            and matrix[i_][j_] != -1 and next_pos not in visited

    right = (i, j + 1)
    left = (i, j - 1)
    down = (i + 1, j)
    up = (i - 1, j)
    for direction in (right, left, up, down):
        if check_(direction):
            free_walker(matrix, direction, visited)


def check(matrix, visited):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i, j) not in visited and matrix[i][j] != -1:
                return False
    return True


def isReachable(field, end):
    visited = set()
    free_walker(field, end, visited)
    return check(field, visited)


# checks
field3 = [
    [ 0,  0,  0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0,  0,  0, 0 ],
]
field5 = [
    [0],
]


assert isReachable(field3, (0, 0)) == False
assert isReachable(field3, (3, 3)) == False
assert isReachable(field5, (0, 0)) == True
