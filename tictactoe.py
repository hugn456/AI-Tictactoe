"""
Tic Tac Toe Player
"""

import math
import copy
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
    empty_count=0
    for row in board:
        for cell in row:
            if cell==EMPTY:
                empty_count+=1
    if (empty_count % 2 ==1):
        
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set=set()
    for row in range(3):
        for cell in range(3):
            if board[row][cell]== EMPTY:
                action_set.add((row,cell))
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    Player=player(board)
    new_board=copy.deepcopy(board)
    try:  
        if new_board[action[0]][action[1]]!=EMPTY or isinstance(action,tuple)==False:
            raise ValueError
        else:
            new_board[action[0]][action[1]]=Player
            return new_board
    except ValueError :
        pass
        
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    left_diagonal_X_count=0
    left_diagonal_O_count=0
    right_diagonal_X_count=0
    right_diagonal_O_count=0
    for i in range(3):
        horizontal_X_count=0
        horizontal_O_count=0
        vertical_X_count=0
        vertical_O_count=0
        for j in range(3):
            if board[i][j]==X:
                horizontal_X_count+=1
            elif board[i][j]==O:
                horizontal_O_count+=1
                
            if board[j][i]==X:
                vertical_X_count+=1
            elif board[j][i]==O:
                vertical_O_count+=1
                
            if i==j and board[i][j]==X:
                left_diagonal_X_count+=1
            elif i==j and board[i][j]==O:
                left_diagonal_O_count+=1

            if (i+j)==2 and board[i][j]==X:
                right_diagonal_X_count+=1
            elif (i+j)==2 and board[i][j]==O:
                right_diagonal_O_count+=1
            
        if horizontal_X_count==3 or vertical_X_count==3 or left_diagonal_X_count==3\
           or right_diagonal_X_count ==3:
            return X
        elif horizontal_O_count==3 or vertical_O_count==3 or left_diagonal_O_count==3\
           or right_diagonal_O_count ==3:
            return O
    return None
        
            
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    Winner=winner(board)
    possible_actions=actions(board)
    if Winner==X or Winner==O or len(possible_actions)==0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        Winner=winner(board)
        if Winner == X:
            return 1
        elif Winner==O:
            return -1
        else:
            return 0

    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        
        Player=player(board)
        Actions=list(actions(board))
        if Player==X:
            vmax=-math.inf
            index=0
            for i in range(len(Actions)):
                minn=minvalue(result(board,Actions[i]))
                if minn>vmax:
                    index=i
                    vmax=minn
        elif Player==O:
            vmin=math.inf
            index=0
            for i in range(len(Actions)):
                maxx=maxvalue(result(board,Actions[i]))
                if vmin> maxx:
                    index=i
                    vmin=maxx
    return Actions[index]
    

def maxvalue(board):
    if terminal(board):
        return utility(board)
    v=-math.inf
    for action in actions(board):
        v=max(v,minvalue(result(board,action)))
    return v

def minvalue(board):
    if terminal(board):
        return utility(board)
    v=math.inf
    for action in actions(board):
        v=min(v,maxvalue(result(board,action)))
    return v

        
