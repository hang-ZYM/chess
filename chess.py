import numpy as np
#大改9.12
#方法出现明显错误
#
# 大改9.12

board_size=8

matrix_size  =  8
if __name__ == '__main__':
    print("process is running!")

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[Node_Status() for _ in range(columns)] for _ in range(rows)]

    def __getitem__(self, key):
        x, y = key
        return self.data[x][y]

    def __setitem__(self, key, value):
        x, y = key
        self.data[x][y] = value

class Node_Status:
    def __init__(self):
        self.status = 0
        self.row_status = 0
        self.col_status = 0
        self.vec_t_status = 0
        self.vec_h_status = 0

class Player:
    def __init__(self,x) :
        self.matrix = Matrix(matrix_size, matrix_size)
        self.legal_move=[]
        self.legal_jump=[]
        self.value=x
   
    
    #可能的错误
    '''def append_move(key,self):
        self.legal_move.append(key)
    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    def __setattr__(self, name, value):
        self.data[name] = value'''


def prepare(player,player2,board):
    if player.legal_move==[]:
        return 
    i=np.random.randint(0,len(player.legal_move))
    [row,col]=player.legal_move[i]
    #for (x,y) in player.legal_jump[i]:
        #if board[x,y]==-player.value:
    if move(player,row,col,board):
        change_status(player,row,col,player2,board)
    #调试
    print(board)
    print(player.legal_move)  
    print(player2.legal_move)  
    
    del player.legal_jump[i]
    del player.legal_move[i]

def flip(player,row,col,directions,board):
    for dr, dc in directions:
            r, c = row + dr, col + dc
            to_flip = []
            while 0 <= r < board_size and 0 <= c < board_size and board[r,c] == -player.value:
                to_flip.append((r, c))
                r += dr
                c += dc
            if 0 <= r < board_size and 0 <= c < board_size and board[r,c] == player.value:
                for flip_row, flip_col in to_flip:
                    board[flip_row,flip_col] = player.value
                return True
            return False

def move(player,row,col,board):
    b_row,b_col,b_vec_h,b_vec_t=False,False,False,False
    if player.matrix[row,col].row_status==1:
        directions = [(0, 1), (0, -1)]
        b_row=flip(player,row,col,directions,board)
    if player.matrix[row,col].col_status==1:
        directions = [(1,0),(-1,0)]
        b_col=flip(player,row,col,directions,board)
    if player.matrix[row,col].vec_h_status==1:
        directions = [(1,1),(-1,-1)]
        b_vec_h=flip(player,row,col,directions,board)
    if player.matrix[row,col].vec_h_status==1:
        directions = [(1,-1),(-1,1)]
        b_vec_t=flip(player,row,col,directions,board)
    if b_row or b_col or b_vec_h or b_vec_t:
         board[row,col]=player.value  
         return True
    return False
    
    
def change_status(player,row,col,player2,board):
    player.matrix[row,col].status=0
    player2.matrix[row,col].status=0
    
    change_row_status(board,row,col,player,player2)
    change_row_status(board,row,col,player,player2)
    change_vec_h_status_(board,row,col,player,player2)
    change_vec_t_status(board,row,col,player,player2)
    
#行状态改变
#'''还没有写对面的状态改变'''--写了 -9-11
#看不懂了，有时间回来写注释  23.9.12
def change_row_status(board,row,col,player,player2):
    if col!=0 and board[row,col-1]==player2.value:
        for i in range(col-2,-1,-1):
            if board[row,i]==0:
                player.matrix[row,i].row_status=1   
                ####
                '''
                if (row,i) in player.legal_move:
                    player.legal_jump[player.legal_move.index([row,i])].append([row,i+1])
                    break'''
                #添加进legal_move
                player.legal_move.append([row,i])
                #player.legal_jump.append([[row,i+1]])
                ####           
                break
            if board[row,i]==player.value:
                break
        
        for i in range(col+1,board_size):
            if board[row,i]==0:
                player2.matrix[row,i].row_status=1
                ####
                #player2.legal_jump.append(row,i-1)
                if (row,i) in player2.legal_move:
                    player2.legal_jump[player2.legal_move.index([row,i])].append([row,i-1])
                    break
                #添加进legal_move
                player2.legal_move.append([row,i])
                player2.legal_jump.append([[row,i-1]])
                ####           
                
                break
            if board[row,i]==player2.value:
                break
    
    if col!=board_size-1 and board[row,col+1]==player2.value:
        for i in range(col+2,board_size):
            if board[row,i]==0:
                player.matrix[row,i].row_status=1
                ####
                #player.legal_jump.append(row,i-1)
                if (row,i) in player.legal_move:
                    player.legal_jump[player.legal_move.index([row,i])].append([row,i-1])
                    break
                #添加进legal_move
                player.legal_move.append([row,i])
                player.legal_jump.append([[row,i-1]])
                ####   
                break
            if board[row,i]==player.value:
                break
        
        for i in range(col-1,-1,-1):
            if board[row,i]==0:
                player2.matrix[row,i].row_status=1
                ####
                #player2.legal_jump.append(row,i+1)
                if (row,i) in player2.legal_move:
                    player2.legal_jump[player2.legal_move.index([row,i])].append([row,i+1])
                    break
                #添加进legal_move
                player2.legal_move.append([row,i])
                player2.legal_jump.append([[row,i+1]])
                ####   
                
                break
            if board[row,i]==player2.value:
                break



def change_col_status(board,row,col,player,player2):
    if row!=0 and board[row-1,col]==player2.value:
        for i in range(row-2,-1,-1):
            if board[i,col]==0:
                player.matrix[i,col].col_status=1
                ####
                #player.legal_jump.append((i+1,col))
                if (i,col) in player.legal_move:
                    player.legal_jump[player.legal_move.index([i,col])].append([i+1,col])
                    break
                #添加进legal_move
                player.legal_move.append([i,col])
                player.legal_jump.append([[i+1,col]])
                ####     
                break
            if board[i,col]==player.value:
                break
        
        for i in range(row+1,board_size):
            if board[i,col]==0:
                player2.matrix[i,col].col_status=1
                ####
                #player2.legal_jump.append((i-1,col))
                if (i,col) in player2.legal_move:
                    player2.legal_jump[player2.legal_move.index([i,col])].append([i-1,col])
                    break
                #添加进legal_move
                player2.legal_move.append([i,col])
                player2.legal_jump.append([[i-1,col]])
                ####   
                break
            if board[i,col]==player2.value:
                break
    
    if row!=board_size-1 and board[row+1,col]==player2.value:
        for i in range(row+2,board_size):
            if board[i,col]==0:
                player.matrix[i,col].col_status=1
                ####
                #player.legal_jump.append((i-1,col))
                if (i,col) in player.legal_move:
                    player.legal_jump[player.legal_move.index([i,col])].append([i-1,col])
                    break
                #添加进legal_move
                player.legal_move.append([i,col])
                player.legal_jump.append([[i-1,col]])
                ####     
                break
            if board[i,col]==player.value:
                break
        
        for i in range(row-1,-1,-1):
            if board[i,col]==0:
                player2.matrix[i,col].col_status=1
                ####
                #player2.legal_jump.append((i+1,col))
                if (i,col) in player2.legal_move:
                    player2.legal_jump[player2.legal_move.index([i,col])].append([i+1,col])
                    break
                #添加进legal_move
                player2.legal_move.append([i,col])
                player2.legal_jump.append([[i+1,col]])
                ####   
                break
            if board[i,col]==player2.value:
                break
       
def change_vec_h_status_(board,row,col,player,player2):
    if row!=board_size-1 and col!=board_size-1 and board[row+1,col+1]==player2.value:
        x=row+2
        y=col+2
        while x!=board_size and y!= board_size:
            if board[x,y]==0:
                player.matrix[x,y].vec_h_status=1
                ####
                #player.legal_jump.append((x-1,y-1))
                if (x,y) in player.legal_move:
                    player.legal_jump[player.legal_move.index([x,y])].append([x-1,y-1])
                    break
                #添加进legal_move
                player.legal_move.append([x,y])
                player.legal_jump.append([[x-1,y-1]])
                ####   
                break
            if board[x,y]==player.value:
                break
            x+=1
            y+=1
       
        x=row-1
        y=col-1
        while x!=-1 and y!=-1:
            if board[x,y]==0:
                player2.matrix[x,y].vec_h_status=1
                ####
                #player2.legal_jump.append((x+1,y+1))
                if (x,y) in player2.legal_move:
                    player2.legal_jump[player.legal_move.index([x,y])].append([x+1,y+1])
                    break
                #添加进legal_move
                player2.legal_move.append([x,y])
                player2.legal_jump.append([[x+1,y+1]])
                ####   
                break
            if board[x,y]==player2.value:
                break
            x-=1
            y-=1
    
    if row!=0 and col!=0 and board[row-1,col-1]==player2.value:
        x=row-2
        y=col-2
        while x!=-1 and y!=-1:
            if board[x,y]==0:
                player.matrix[x,y].vec_h_status=1
                ####
                #player.legal_jump.append((x+1,y+1))
                if (x,y) in player.legal_move:
                    player.legal_jump[player.legal_move.index([x,y])].append([x+1,y+1])
                    break
                #添加进legal_move
                player.legal_move.append([x,y])
                player.legal_jump.append([[x+1,y+1]])
                ####   
                break
            if board[x,y]==player.value:
                break
            x-=1
            y-=1
        
        x=row+1
        y=col+1
        while x!=board_size and y!=board_size:
            if board[x,y]==0:
                player2.matrix[x,y].vec_h_status=1
                ####
                #player2.legal_jump.append((x-1,y-1))
                if (x,y) in player2.legal_move:
                    player2.legal_jump[player.legal_move.index([x,y])].append([x-1,y-1])
                    break
                #添加进legal_move
                player2.legal_move.append([x,y])
                player2.legal_jump.append([[x-1,y-1]])
                ####   
                break
            if board[x,y]==player2.value:
                break
            x+=1
            y+=1


def change_vec_t_status(board,row,col,player,player2):
    if row!=0 and col!=board_size-1 and board[row-1,col+1]==player2.value:
        x=row-2
        y=col+2
        while x!=-1 and y!=board_size:
            if board[x,y]==0:
                player.matrix[x,y].vec_t_status=1
                ####
                #player.legal_jump.append((x+1,y-1))
                if (x,y) in player.legal_move:
                    player.legal_jump[player.legal_move.index([x,y])].append([x+1,y-1])
                    break
                #添加进legal_move
                player.legal_move.append([x,y])
                player.legal_jump.append([[x+1,y-1]])
                ####   
                break
            if board[x,y]==player.value:
                break
            x-=1
            y+=1
       
        x=row+1
        y=col-1
        while x!=board_size and y!=-1:
            if board[x,y]==0:
                player2.matrix[x,y].vec_t_status=1
                ####
                #player2.legal_jump.append((x-1,y+1))
                if (x,y) in player2.legal_move:
                    player2.legal_jump[player.legal_move.index([x,y])].append([x-1,y+1])
                    break
                #添加进legal_move
                player2.legal_move.append([x,y])
                player2.legal_jump.append([[x-1,y+1]])
                ####   
                break
            if board[x,y]==player2.value:
                break
            x+=1
            y-=1
    if row!=board_size-1 and col!=0 and board[row+1,col-1]==player2.value:
        x=row+2
        y=col-2
        while x!=board_size and y!=-1:
            if board[x,y]==0:
                player.matrix[x,y].vec_t_status==1
                ####
                #player.legal_jump.append((x-1,y+1))
                if (x,y) in player.legal_move:
                    player.legal_jump[player.legal_move.index([x,y])].append([x-1,y+1])
                    break
                #添加进legal_move
                player.legal_move.append([x,y])
                player.legal_jump.append([[x-1,y+1]])
                ####   
                break
            if board[x,y]==player.value:
                break
            x+=1
            y-=1
        
        x=row-1
        y=col+1
        while x!=-1 and y!=board_size:
            if board[x,y]==0:
                player2.matrix[x,y].vec_t_status=1
                ####
                #player2.legal_jump.append((x+1,y-1))
                if (x,y) in player2.legal_move:
                    player.legal_jump[player.legal_move.index([x,y])].append([x+1,y-1])
                    break
                #添加进legal_move
                player2.legal_move.append([x,y])
                player2.legal_jump.append([[x+1,y-1]])
                ####   
                break
            if board[x,y]==player2.value:
                break
            x-=1
            y+=1
