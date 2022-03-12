import random

player1 = input("Enter player1 name: ")
player2 = input("Enter player2 name: ")
board = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
moves = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
exit=False
p1w=p2w=0
def toss():
    tosswin = random.randint(1,3)
    if(tosswin == 1):
        print(player1,"won the toss, Plays X first")
        p1=True
    else:
        print(player2,"won the toss, Plays X first")
        p2=True

toss()

def printBoard():
    for i in range(3):
        print(*board[i],end='\n')

def evaluateRes():
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='X'):
                p1w=p1w+1
        if(p1w==3):
            p1win = True
            break
        else:
            p1w = 0
            p1win = False

    for i in range(3):
        for j in range(3):
            if(board[j][i]=='X'):
                p1w=p1w+1
        if(p1w==3):
            p1win = True
            break
        else:
            p1w = 0
            p1win = False



def playPosition1():
    
    pos = int(input("Enter position: "))
    p1win=False
    if(pos<4):
        board[0][pos] = 'X'
    elif(pos<7):
        board[1][pos-3] = 'X'    
    elif(pos<10):
        board[2][pos-6] = 'X'    
    else:
        print("invalid")

    p1win = evaluateRes()

def playPosition2():
    
    pos = int(input("Enter position: "))
    p2win=False
    if(pos<4):
        board[0][pos] = 'O'
    elif(pos<7):
        board[1][pos-3] = 'O'    
    elif(pos<10):
        board[2][pos-6] = 'O'    
    else:
        print("invalid")

    p2win = evaluateRes()

    return p2win
while(exit==False):
    playPosition1()
    playPosition2()
    printBoard()