import chess_p
player=chess_p.Player(1)
player2=chess_p.Player(-1)

player.legal_move=[[3,5],[4,2],[2,4],[5,3]]
player.legal_jump=[[[3,4]],[[4,3]],[[3,4]],[[4,3]]]
player2.legal_move=[[3,2],[4,5],[2,3],[5,4]]
player2.legal_jump=[[[3,3]],[[4,4]],[[3,3]],[[4,4]]]

print("init finished")
if __name__  ==  "__main__":
    print("process is running")