import init_p
import chess_p
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
            m=chess_p.mtcr(player)
            
            m.gen_random_sample(player,player2,board,100)
            a=m.max_a(player)
            if a!=[]:m.transform(board,a,player,player2)
            print(board)
        if player2.legal_move!=[]:
            m=chess_p.mtcr(player2)
            m.gen_random_sample(player2,player,board,100)
            a=m.max_a(player2)
            if a!=[]:m.transform(board,a,player2,player)
            print(board)
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
    game(init_p.player,init_p.player2,board)
    
    




