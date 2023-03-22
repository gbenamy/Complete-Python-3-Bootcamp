from IPython.display import clear_output

def printBoard(data):
    print(data[0:3])
    print(data[3:6])
    print(data[6:9])
    
def checkWin(data):
    #check rows
    pass

    #check columns
    pass

    #check diagonals

def isValid(selection, data,player):
    if selection.isdigit() == False:
        print("Not a digit!")
        return False
    if int(selection) not in range (1,10):
        print ("Not in range!")
        return False
    if data[int(selection)] != '   ':
        print("Already taken!")
        return False
    if player == 1:
        data[int(selection)] = ' X '
    else:
        data[int(selection)] = ' O '
    
    



data =[' X ',' O ','   ',' O ',' X ',' X ',' O ',' X ',' O ']

def startGame():
    gameEnded = False
    player=1
    moves=0

    while not gameEnded:
        valid=False
        while not valid:
            clear_output()
            printBoard(data)
            selection=input(f'player{player} please select a position (1-9):')
            valid = isValid(selection,data,player)


startGame()
