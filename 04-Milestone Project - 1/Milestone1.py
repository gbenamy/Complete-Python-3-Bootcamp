from IPython.display import clear_output

def printBoard(data,demo=False):
    temp = data[:]
    if not demo:

        for index,value in enumerate (data):
            if data[index]==1:
                temp[index]='X'
            elif data[index]==2:
                temp[index]='O'
            else:
                temp[index]=' '

    print(" {} | {} | {} ".format(temp[0],temp[1],temp[2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(temp[3],temp[4],temp[5]))
    print("---|---|---")
    print(" {} | {} | {} ".format(temp[6],temp[7],temp[8]))
    
    
def checkWin(data):
    #check rows
    pass

    #check columns
    pass

    #check diagonals

    return False

def printHelp():
    print("Board Positions:")
    print("----------------")
    printBoard([1,2,3,4,5,6,7,8,9],True)
    print("print 'help' to see it again\n")


def isValid(selection, data,player):
    if selection == 'help':
        printHelp()
        return False
    if selection.isdigit() == False:
        print("Not a digit!")
        return False
    if int(selection) not in range (1,10):
        print ("Not in range!")
        return False
    if data[int(selection)] != 0:
        print("Already taken!")
        return False
    data[int(selection)-1] = player

    
#  1 | 2 | 3 
# ---|---|---
#  4 | 5 | 6 
# ---|---|---
#  7 | 8 | 9 

data =[1,0,1,0,2,0,0,2,0]

def startGame():
    data=[0,0,0,0,0,0,0,0,0]
    gameEnded = False
    player=1
    moves=0

    while not gameEnded:
        valid=False
        selection = 0
        while not valid:
            clear_output()
            printBoard(data)
            selection=input(f'player{player} please select a position (1-9):')
            valid = isValid(selection,data,player)
        data[selection]=player
        gameEnded = checkWin()
        if (player==1):
            player=2
        else:
            player=1
        moves+=1
        if moves==9:
            print("Board is full!\nNo one won")
            gameEnded=True
        
printHelp()
startGame()
