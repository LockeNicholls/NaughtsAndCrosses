running = True
game = False
whitespace=" "
playerPiece = "X"
computerPiece = "O"
counter = 0

def printBoard():
    print("   0  1  2 ")
    print("0  "+board[0][0]+"|"+board[1][0]+" |"+board[2][0]+"  ")
    print("  ---------")
    print("1  "+board[0][1]+"|"+board[1][1]+" |"+board[2][1]+"")
    print("  ---------")
    print("2  "+board[0][2]+"|"+board[1][2]+" |"+board[2][2]+"")

def winDetect(piece):
    #Check verticals and horizontals
    for i in range(3):
        if (board[i][0]==piece)&(board[i][1]==piece)&(board[i][2]==piece):            
            return True
        elif (board[0][i]==piece)&(board[1][i]==piece)&(board[2][i]==piece):
            return True;
    #Check diagonals
    if (board[0][0]==piece)&(board[1][1]==piece)&(board[2][2]==piece):            
        return True
    if (board[0][2]==piece)&(board[1][1]==piece)&(board[2][0]==piece):            
        return True       

    #If you haven't won yet, you haven't won
    return False
    
def detect2(piece):
    #upper left
    for x in range(3):
        for y in range(3):
            if (board[x][y]==piece):
                #Check left
                if (x-1 in range(3)):
                    if (board[x-1][y]==piece):
                        if (x-2 in range(3)):
                            if (board[x-2][y]==whitespace):
                                return (x-2,y)
                #Check right
                if (x+1 in range(3)):
                    if (board[x+1][y]==piece):
                        if (x+2 in range(3)):
                            if (board[x+2][y]==whitespace):
                                return (x+2,y)
                #Check above
                if (y-1 in range(3)):
                    if (board[x][y-1]==piece):
                        if (y-2 in range(3)):
                            if (board[x][y-2]==whitespace):
                                return (x,y-2)
                #Check below
                if (y+1 in range(3)):
                    if (board[x][y+1]==piece):
                        if (y+2 in range(3)):
                            if (board[x][y+2]==whitespace):
                                return (x,y+2)

                #Check diag up left
                if ((x-1 in range(3))&(y-1 in range(3))):
                    if (board[x-1][y-1]==piece):
                        if ((x-2 in range(3))&(y-2 in range(3))):
                            if (board[x-2][y-2]==whitespace):
                                return (x-2,y-2)
                #Check diag up right
                if ((x+1 in range(3))&(y-1 in range(3))):
                    if (board[x+1][y-1]==piece):
                        if ((x+2 in range(3))&(y-2 in range(3))):
                            if (board[x+2][y-2]==whitespace):
                                return (x+2,y-2)

                #Check diag down left
                if ((x-1 in range(3))&(y+1 in range(3))):
                    if (board[x-1][y+1]==piece):
                        if ((x-2 in range(3))&(y+2 in range(3))):
                            if (board[x-2][y+2]==whitespace):
                                return (x-2,y+2)

                #Check diag down right
                if ((x+1 in range(3))&(y+1 in range(3))):
                    if (board[x+1][y+1]==piece):
                        if ((x+2 in range(3))&(y+2 in range(3))):
                            if (board[x+2][y+2]==whitespace):
                                return (x+2,y+2)
                            

    return (-1,-1)
##def detectFork():
##    #Checking center-corner forks (perhaps these are the only ones, just the first thing I thought of) 
##    #Check the center is a player piece
##    if board[1][1]==playerPiece:
##        if board[0][0]==playerPiece
##            if (board[1][0]==whitespace & board[2][0]==whitespace & board [1][2] ==whitespace):
##                return(2,0)
##            if (board[1][0]==whitespace & board[2][0]==whitespace & board [1][2] ==whitespace):
##                return(2,0)
##
##
##        if (board[
##            
                

    


def detectOppositeCorner(piece):
    if board[0][0]==piece:
        if board[2][2]==whitespace:
            return(2,2)

    if board[2][0]==piece:
        if board[0][2]==whitespace:
            return(0,2)

    if board[2][2]==piece:
        if board[0][0]==whitespace:
            return(0,0)

    if board[0][2]==piece:
        if board[2][0]==whitespace:
            return(2,0)

    return(-1,-1)

def detectCorner():
    if board[0][0]==whitespace:
            return(0,0)

    if board[2][0]==whitespace:
            return(2,0)

    if board[2][2]==whitespace:
            return(2,2)

    if board[0][2]==whitespace:
            return(0,2)

    return(-1,-1)
                        
def detectSide():
    if board[1][0]==whitespace:
            return(1,0)

    if board[2][1]==whitespace:
            return(2,1)

    if board[1][2]==whitespace:
            return(1,2)

    if board[0][1]==whitespace:
            return(0,1)

    return(-1,-1)

while running:
    board = [[whitespace for x in range(3)] for y in range(3)] 
    print();
    choice=input("Do you want to play a round? y/n\n")
    if ((choice !="y") & (choice!= "n")):
        print("y or n")
    elif (choice=="n"):
        running=False
    elif (choice=="y"):
        game = True
        counter = 0
        
        printBoard()

    while game:           
        pturn = True;
        print()
        print("Player turn")
        counter+=1
        if counter <8:
            print 
        while pturn:
        
            x=int(input("Enter x coord: "))
            y=int(input("Enter y coord: "))
            print()
            if (board[x][y]==whitespace):
                board[x][y]=playerPiece
                print(detect2(playerPiece))
                pturn=False;
            else:
                print("Already something there")                    
            printBoard()
            if winDetect(playerPiece):
                print("Player Wins")
                pturn=False
                game=False

        cturn=True;
        print()
        print("Computer Turn")
        counter+=1
        while cturn:
            
            #Check for win
            output = detect2(computerPiece)
            if output!=(-1,-1):                
                board[output[0]][output[1]]=computerPiece
                print()                   
                printBoard()
                cturn=False;
                break
            #Check for block
            output = detect2(playerPiece)
            if output!=(-1,-1):                
                board[output[0]][output[1]]=computerPiece
                print()                   
                printBoard()
                cturn=False
                break

            #check for fork
            #check for fork block

            #Check for center
            if board[1][1]==whitespace:
                board[1][1]=computerPiece
                print()                   
                printBoard()
                cturn=False
                break

            #Check for opposite corner
            output = detectOppositeCorner(playerPiece)
            if output!=(-1,-1):
                board[output[0]][output[1]]=computerPiece
                print()                   
                printBoard()
                cturn=False
                break

            #check free corner
            output = detectCorner()
            if output!=(-1,-1):
                board[output[0]][output[1]]=computerPiece
                print()                   
                printBoard()
                cturn=False
                break

            #check free side
            output = detectSide()
            if output!=(-1,-1):
                board[output[0]][output[1]]=computerPiece
                
                cturn=False
                break
                
                

            if winDetect(computerPiece):
                print("Computer Wins")
                cturn=False
                game=False
            cturn=False;


