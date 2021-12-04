
# Description

import os
import sys

__inputfile__ = 'input.txt'
__location__ = os.path.join(sys.path[0], __inputfile__)

with open(__location__, 'r') as f:
    input_str = f.read().strip() # Takes the inputfile as a string

test = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

def parse(inp):
    input = inp.split('\n\n')
    numbers = list(map(int, input[0].split(',')))
    input = list(map(lambda x: list(map(lambda y: (int(y), 0), (' '.join(x.split())).split())), input[1:]))
    
    return numbers, input

def mark_board(ball, board):
    for i in range(len(board)):
        if board[i][0] == ball:
            board[i] = (board[i][0],1)
            break
    
def check_winning(board):
    marked = list(zip(*board))[-1]
    for s in range(5):
        row_win, col_win = True, True
        for i in range(5):
            row_win &= marked[5*s + i]
            col_win &= marked[s + 5*i]
        if row_win or col_win:
            return True

def calculate_score(n,board):
    unmarked = list(zip(*filter(lambda t: t[1] == 0, board)))[0]
    return n * sum(unmarked)
    
def play_bingo(balls, boards, first_to_win = True):
    for n in numbers:
        winners = []
        for i,b in enumerate(boards):
            mark_board(n, b)
            if check_winning(b):
                if first_to_win or len(boards) == 1:
                    return calculate_score(n,b)
                else:
                    winners.append(i)
        for j in winners[::-1]:
            del boards[j]


if __name__ == "__main__":
    numbers, boards = parse(input_str)
    # Part 1
    print(play_bingo(numbers, boards))

    # Part 2
    print(play_bingo(numbers, boards, False))
        
    