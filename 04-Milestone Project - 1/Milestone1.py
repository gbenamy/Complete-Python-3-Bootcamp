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
#  0 | 1 | 2 
# ---|---|---
#  3 | 4 | 5 
# ---|---|---
#  6 | 7 | 8 

    #check rows
    for index in range(3):
        if ((data[0+index*3]==data[1+index*3]==data[2+index*3]) and data[0+index*3]!=0):
            return True

    #check columns
    for index in range(3):
        if ((data[0+index]==data[3+index]==data[6+index]) and data[0+index]!=0):
            return True

    #check diagonals
    if (((data[0]==data[4]==data[8]) and data[0]!=0) or ((data[2]==data[4]==data[6]) and data[2]!=0)):
        return True 

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
    if data[int(selection)-1] != 0:
        print("Already taken!")
        return False
    data[int(selection)-1] = player
    return True
    
#  1 | 2 | 3 
# ---|---|---
#  4 | 5 | 6 
# ---|---|---
#  7 | 8 | 9 

data =[1,0,1,0,2,0,0,2,0]

def startGame(debug=False):
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
        if (checkWin(data)):
            gameEnded=True
            printBoard(data)
            print(f'Player{player} has won!')
            break
        
        if (player==1):
            player=2
        else:
            player=1
        moves+=1
        if moves==9:
            print("Board is full!\nNo one won")
            printBoard(data)
            gameEnded=True
        
printHelp()
startGame()
