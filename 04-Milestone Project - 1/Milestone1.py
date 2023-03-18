def printBoard(data):
    print(data[0:3])
    print(data[3:6])
    print(data[6:9])

def validateSelection(data,position):
    if (data[position]=='   '):
        return True
    else:
        return False
    
def checkWin(data):
    #check rows
    for

    #check columns
    for

    #check diagonals

data =[' X ',' O ','   ',' O ',' X ',' X ',' O ',' X ',' O ']
printBoard(data)
validateSelection(data,2)

def startGame():
    gameEnded = False
    player=1
    moves=0

    while not gameEnded:
        valid=False
        while not valid
        selection=input(f'player{player} please select a position (1-9):')



