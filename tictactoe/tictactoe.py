"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    delta = 0
    for row in board:
        for col in row:
            if col == X:
                delta += 1
            elif col == O:
                delta -= 1
    if delta == 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    row = 0
    col = 0
    actions = []
    for x in board:
        for y in x:
            if y == EMPTY:
                action = [row, col]
                actions.append(action)
            col += 1
        row += 1
        col = 0
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temp = copy(board)
    if not temp[action[0]][action[1]] == EMPTY:
        raise Exception("invalid action")
    temp[action[0]][action[1]] = player(board)
    print(temp)
    print(board)
    return temp

def copy(old):
    new = []
    for row in old:
        temp = []
        for col in row:
            temp.append(col)
        new.append(temp)
    return new

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[1][1]
    elif board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return board[2][0]
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) == X or winner(board) == O or not any(EMPTY in row for row in board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    list = actions(board)
    states = []
    for action in list:
        temp = result(board, action)
        x = state(temp)
        states.append(x)
    turn = player(board)
    return list[states.index(max(states))] if turn == X else list[states.index(min(states))]

def state(board):
    if terminal(board):
        return utility(board)
    return state(result(board, minimax(board)))
