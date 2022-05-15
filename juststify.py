def printTable(itemsDict, leftWidth, rightWidth):
    print('LEADER BOARD'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}



LeaderBoard={'Gamer Snave':67, 'Belyon': 50, 'Creep':40, 'Boobie':31}

# printTable(LeaderBoard, 20, 20)


for i,j in LeaderBoard.items():
    print(i.ljust(20, '.') + str(j).rjust(20, ' '))
    
def printBoard(itemsDict,lw,rw):
    for i,j in itemsDict.items():
        print(i.ljust(lw, '*')+ str(j).rjust(rw, ' '))

printBoard(LeaderBoard, 20, 20)
        