import chess

player=chess.Player(1)
player2=chess.Player(-1)
player.matrix[3,5].status=1
player.matrix[4,2].status=1
player.matrix[2,4].status=1
player.matrix[5,3].status=1

player2.matrix[3,2].status=1
player2.matrix[4,5].status=1
player2.matrix[2,3].status=1
player2.matrix[5,4].status=1

player.matrix[3,5].row_status=1
player.matrix[4,2].row_status=1
player.matrix[5,3].col_status=1
player.matrix[2,4].col_status=1

player2.matrix[3,2].row_status=1
player2.matrix[4,5].row_status=1
player2.matrix[2,3].col_status=1
player2.matrix[5,4].col_status=1

player.legal_move=[[3,5],[4,2],[2,4],[5,3]]
player.legal_jump=[[[3,4]],[[4,3]],[[3,4]],[[4,3]]]
player2.legal_move=[[3,2],[4,5],[2,3],[5,4]]
player2.legal_jump=[[[3,3]],[[4,4]],[[3,3]],[[4,4]]]

print("init finished")
if __name__  ==  "__main__":
    print("process is running")
