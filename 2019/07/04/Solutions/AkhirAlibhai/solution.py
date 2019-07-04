import copy


def get_neighbours(board, coordinate, dimensions):
    neighbours = []

    # There is a neighbour at coordinate[0]+1,coordinate[1]
    if not coordinate[0] == dimensions[0] - 1:
        neighbours.append((coordinate[0]+1, coordinate[1]))

    # There is a neighbour at coordinate[0],coordinate[1]+1
    if not coordinate[1] == dimensions[1] - 1:
        neighbours.append((coordinate[0], coordinate[1]+1))

    # There is a neighbour at coordinate[0]-1,coordinate[1]
    if not coordinate[0] == 0:
        neighbours.append((coordinate[0]-1, coordinate[1]))

    # There is a neighbour at coordinate[0],coordinate[1]-1
    if not coordinate[1] == 0:
        neighbours.append((coordinate[0], coordinate[1]-1))

    return neighbours


def check_new_letter(board, coordinate, dimensions, word):
    if not word:
        return True

    # Returns the coordinates of the adjacent elements
    neighbours = get_neighbours(board, coordinate, dimensions)
    for neighbour in neighbours:
        # If the element matches the next letter in the word
        if board[neighbour[0]][neighbour[1]] == word[0]:
            # Deep copies cause python needs this :|
            copy_board = copy.deepcopy(board)
            copy_board[neighbour[0]][neighbour[1]] = 0

            # To make sure we are able to check all neighbours
            if check_new_letter(copy_board, neighbour, dimensions, word[1:]):
                return True

    return False


def find_word_in_board(board, word):
    dimensions = (len(board), len(board[0]))

    for row in range(0, dimensions[0]):
        for column in range(0, dimensions[1]):
            if board[row][column] == word[0]:
                # Deep copies cause python needs this :|
                copy_board = copy.deepcopy(board)
                copy_board[row][column] = 0

                # To make sure we can check all elements in the board
                if check_new_letter(copy_board, (row, column),
                                    dimensions, word[1:]):
                    return True
    return False