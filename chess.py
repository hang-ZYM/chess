import torch
import numpy as np


# 定义棋盘大小和初始局面
board_size=8
board=np.zeros((board_size,board_size))
board[3,3]=1
board[4,4]=1
board[3,4]=-1
board[4,3]=-1
board_tensor=torch.tensor(board)
print(board)
#行状态
row_status=np.zeros((board_size,board_size))
#列状态
col_status=np.zeros((board_size,board_size))
#斜状态
vec_h_status=np.zeros((board_size,board_size))
vec_t_status=np.zeros((board_size,board_size))
#初始化状态
def init_status(row,col,row_status,col_status,vec_status):
    row_status[3,2]=-1
    row_status[4,5]=-1
    row_status[3,5]=1
    row_status[4,2]=1
    col_status[2,3]=-1
    col_status[5,3]=1
    col_status[2,4]=1
    col_status[5,4]=-1
#行状态改变
'''还没有写对面的状态改变'''
def change_row_status(board,row,col,row_status,player):
    row_status[row,col]=0
    if col!=0 and board[row,col-1]==-player:
        for i in range(col-2,-1,-1):
            if board[row,i]==0:
                row_status[row,i]=player
                break
            if board[row,i]==player:
                break
        if col!=board_size-1:
            for i in range(col+1,board_size):
                if board[row,i]==0:
                    row_status[row,i]=-player
                    break
                if board[row,i]==-player:
                    break
    if col!=board_size-1 and board[row,col+1]==-player:
        for i in range(col+2,board_size):
            if board[row,i]==0:
                row_status[row,i]=player
                break
            if board[row,i]==player:
                break
        if col!=0:
            for i in range(col-1,-1,-1):
                if board[row,i]==0:
                    row_status[row,i]=-player
                    break
                if board[row,i]==-player:
                    break



def change_col_status(board,row,col,col_status,player):
    col_status[row,col]=0
    if row!=0 and board[row-1,col]==-player:
        for i in range(row-2,-1,-1):
            if board[i,col]==0:
                col_status[i,col]=player
                break
            if board[i,col]==player:
                break
        if row!=board_size-1:
            for i in range(row+1,board_size):
                if board[i,col]==0:
                    col_status[i,col]=-player
                    break
                if board[i,col]==-player:
                    break
    if row!=board_size-1 and board[row+1,col]==-player:
        for i in range(row+2,board_size):
            if board[i,col]==0:
                col_status[i,col]=player
                break
            if board[i,col]==player:
                break
        if row!=0:
            for i in range(row-2,-1,-1):
                if board[i,col]==0:
                    col_status[i,col]=-player
                    break
                if board[i,col]==-player:
                    break
           
def change_vec_h_status_(board,row,col,vec_h_status,player):
    vec_h_status[row,col]=0
    if row!=board_size-1 and col!=board_size-1 and board[row+1,col+1]==-player:
        x=row+2
        y=col+2
        while x!=board_size and y!= board_size:
            if board[x,y]==0:
                vec_h_status=player
                break
            if board[x,y]==player:
                break
            x+=1
            y+=1
        if row!=0 and col!=0:
            x=row-1
            y=col-1
            while x>=0 and y>=0:
                if board[x,y]==0:
                    vec_h_status=-player
                    break
                if board[x,y]==-player:
                    break
    if row!=0 and col!=0 and board[row-1,col-1]==-player:
        x=row-2
        y=col-2
        while x!=-1 and y!=-1:
            if board[x,y]==0:
                vec_h_status=player
                break
            if board[x,y]==player:
                break
            x-=1
            y-=1
        if row!=board_size-1 and col!=board_size-1:
            x=row+1
            y=col+1
            

def change_status(row,col,row_status,col_status,vec_status):
    row_status[row,col]=0
    col_status[row,col]=0
    vec_status[row,col]=0

    

def find_all_moves(board,chess_l):
    for row in range(board_size):
        for col in range(board_size):