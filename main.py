import numpy as np 
import random
from time import sleep 

def main():
	print('Welcome to my TicTacToe program!')

if __name__ == '__main__':
	main()

def board():
	return(np.array[[0, 0, 0],
			        [0, 0, 0],
			        [0, 0, 0]])

def possible(board):
	l = []

	for i in range(len(board)):
		for j in range(len(board)):

			if board[i][j] == 0:
				l.append(i,j):
	return (l)

def random_spot(board , player):
	select = possible(board)
	current = random.choice(select)
	board[current] = player
	return(board)

def row_win():
	for x in range(len(board)):
		win = True

		for y in range(len(board)):
			if board[x,y] != player:
			win = False
			continue

		if win == True:
			return win
	return(win)

def col_win():
	for x in range(len(board)):
		win = True

		for y in range(len(board)):
			if board[x,y] != player:
				win = False
				continue

		if win == True:
			return win
	return(win)

def diag_win():
	win = True
	y = 0
	for x in range(len(board)):
		if board[x,x] != player
			win = False

	if win:
		return win
	win = True
	if win:
		for x in range(len(board)):
			y = len(board) - 1 - x
			if board[x,y] != player
				win = False	
	return win

def evaluate(board):
	winner = 0

	for player in [1,2]:
		if (row_win(board,player) or
		   col_win(board,player) or
		   diag_win(board,player))

		  winner = player
	if np.all(board != 0) and winner == 0:
		winner = -1
	return winner

def play():
	board, winner, counter = board(), 0, 1
	print (board)
	sleep(2)

	while winner == 0;
		for player in [1,2]:
			board = random_spot(board,player)
			print ("Board after" + str(counter) + "move")
			print(board)
			sleep(2)
			counter += 1
			winner =. evaluate(board)
			if winner != 0
				break
	return (winner)

print(" Winner is " + str(play()))