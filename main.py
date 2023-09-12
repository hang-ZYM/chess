import init
import chess
import numpy as np

board_size=8

board=np.zeros((board_size,board_size))
board[3,3]=1
board[4,4]=1
board[3,4]=-1
board[4,3]=-1

def game(player,player2,board):
    while player.legal_move!=[] or player2.legal_move!=[]:
        if player.legal_move!=[]:
            chess.prepare(player,player2,board)
        if player2.legal_move!=[]:
            chess.prepare(player2,player,board)
    print(player.legal_move)
    print(player2.legal_move)
    score=0
    for i in range(board_size):
        for j in range(board_size):
            score+=board[i,j]
    print(score)
    print("player1 win" if score>0 else "palyer2 win or no winner")
    
            
if __name__ == '__main__':
    print("game is ready")
    game(init.player,init.player2,board)
    
    




