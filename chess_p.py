import numpy as np
import chess_p
board_size=8
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
if __name__ == '__main__':
    print("process is running!")

class mtcr:
    def __init__(self,player) -> None:
        self.rewards=[100 for _ in range(len(player.legal_move))]
          
    def gen_random_sample(self,player,player2,board,num):
        i=0
        while i!=len(player.legal_move):
            #第一步是否可走，不可走归0
            
            board_copy=board.copy()
            player_copy=chess_p.Player(1)
            player2_copy=chess_p.Player(-1);
            player2_copy.copy(player2)
            player_copy.copy(player)
            if self.transform(board_copy,player_copy.legal_move[i],player_copy,player2_copy):               
                del player.legal_move[i]
                del self.rewards[i]
                continue  
            board_temp=board_copy.copy()  
            player_temp=chess_p.Player(1) 
            player_temp.copy(player_copy)
            player2_temp=chess_p.Player(-1)
            player2_temp.copy(player2_copy)
            for _ in range(num):
                board_copy=board_temp.copy()
                player2_copy.copy(player2_temp)
                player_copy.copy(player_temp) 
                #True 不退出 False 退出 找到action就False             
                while player_copy.legal_move!=[]and player2_copy.legal_move!=[]:
                    t=True
                    while t and player2_copy.legal_move!=[]:
                       
                        x=int(np.random.random()*(len(player2_copy.legal_move)-1))
                        a=player2_copy.legal_move[x] 
                        t=self.transform(board_copy,a,player2_copy,player_copy)
                        if t:del player2_copy.legal_move[x]
                    
                    t=True
                    while t and player_copy.legal_move!=[]:
                        x=int( np.random.random()*(len(player_copy.legal_move)-1))
                        a=player_copy.legal_move[x] 
                        t=self.transform(board_copy,a,player_copy,player2_copy)
                        if t:del player_copy.legal_move[x]
                            
                    
                result=sum(sum(board_copy))
                if result*player.value>0:self.rewards[i]+=1
                else:self.rewards[i]-=1
            i+=1
          
                                   

    def transform(self,board,action,player,player2):
        [row,col]=action
        if  board[row,col] or not self.flip(player,row,col,board,player2):    
            return True
        change_status(player,row,col,player2,board)
        return False
    
    def flip(self,player,row,col,board,player2):
        flip=False
        for dr, dc in directions:
            r, c = row + dr, col + dc
            to_flip = []
            while 0 <= r < board_size and 0 <= c < board_size and board[r,c] == -player.value:
                to_flip.append((r, c))
                r += dr
                c += dc
            if 0 <= r < board_size and 0 <= c < board_size and board[r,c] == player.value and to_flip!=[]:
                for flip_row, flip_col in to_flip:
                    board[flip_row,flip_col] = player.value
                    flip=True
                    change_status(player,flip_row,flip_col,player2,board)
        if flip:
            board[row,col]=player.value
            return True        
        return False
    
    def max_a(self,player):
        if self.rewards==[]:
            return []
        return player.legal_move[self.rewards.index(max(self.rewards))]
        





class Player:      
    def __init__(self,x) :
        #self.matrix = Matrix(board_size, board_size)
        self.legal_move=[]
        self.value=x
    def copy(self,player):
        self.legal_move=player.legal_move.copy()
        self.value=player.value
        
        

def flip(player,row,col,board,player2):
    flip=False
    for dr, dc in directions:
            r, c = row + dr, col + dc
            to_flip = []
            while 0 <= r < board_size and 0 <= c < board_size and board[r,c] == -player.value:
                to_flip.append((r, c))
                r += dr
                c += dc
            if 0 <= r < board_size and 0 <= c < board_size and board[r,c] == player.value and to_flip!=[]:
                for flip_row, flip_col in to_flip:
                    board[flip_row,flip_col] = player.value
                    flip=True
                    change_status(player,flip_row,flip_col,player2,board)
    if flip:
        board[row,col]=player.value
        return True        
    return False


def change_status(player,row,col,player2,board):
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < board_size and 0 <= c < board_size and board[r,c]==player2.value:
            while 0 <= r < board_size and 0 <= c < board_size:
                if  board[r,c] ==0:
                    player.legal_move.append([r,c])
                    break
                if  board[r,c] ==player.value:
                    break
                r += dr
                c += dc
            r=row
            c=col
            while 0 <= r < board_size and 0 <= c < board_size:
                if board[r,c]==0:
                    player2.legal_move.append([r,c])
                    break
                if board[r,c]==player2.value:
                    break
                r-=dr
                c-=dc
                
def prepare(player,player2,board):
    while player.legal_move!=[]:
        i=np.random.randint(0,len(player.legal_move))
        [row,col]=player.legal_move[i]   
        if  board[row,col]==0 and flip(player,row,col,board,player2) :
            
            change_status(player,row,col,player2,board)
            break
        del player.legal_move[i]
    print(board)
    print(player.legal_move)  
    print(player2.legal_move)               
        
            
            