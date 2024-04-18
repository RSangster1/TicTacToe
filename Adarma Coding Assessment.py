#Adarma Coding Assessment
#Robbie Sangster

print("Hello World")


#3x3 grid
grid = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]

def drawGrid():
    for i in range(3):
        print(grid[i])


def playerInput(player):  # Player one enters their turn

    print(player, "Turn")
    square = int(input("enter square 1-9: "))

    if square == 1 or square == 2 or square == 3:
        square -= 1
        row = 0
    elif square == 4 or square == 5 or square == 6:
        square -= 4
        row = 1
    elif square == 7 or square == 8 or square == 9:
        square -= 7
        row = 2
    
    playerValid(row, square, player)

def playerValid(row, square, player): # check if the square is already taken
    if grid[row][square] == "X" or grid[row][square] == "O":
        print("pick another row")
        playerInput()
    else:
        grid[row][square] = player


def checkGrid(player): #Check if three in a row
    if grid[0][0] == grid[0][1] == grid[0][2] == player: #Top row across
        return True
    elif grid[1][0] == grid[1][1] == grid[1][2] == player: #Middle row across
        return True
    elif grid[2][0] == grid[2][1] == grid[2][2] == player: # Bottom row across
        return True
    elif grid[0][0] == grid[1][0] == grid[2][0] == player: #First Column down
        return True
    elif grid[0][1] == grid[1][1] == grid[2][1] == player: # Second Column down 
        return True
    elif grid[0][2] == grid[1][2] == grid[2][2] == player: # Third Column down
        return True
    elif grid[0][0] == grid[1][1] == grid[2][2] == player: #First diagonal 
        return True
    elif grid[0][2] == grid[1][1] == grid[2][0] == player: #Second diagonal
        return True
    else:
        return False

def checkDraw(): # check if game is a draw by having no # in the grid
    for row in grid:
        if "#" in row:
            return False
    return True

drawGrid()

while True: # run until some gets 3 in a row
    playerInput("X")
    drawGrid()
    if checkGrid("X"):
        print("Player X wins")
        break
    elif checkDraw():
        print("draw")
        break
    playerInput("O")
    drawGrid()
    if checkGrid("O"):
        print("Player O wins")
        break
    elif checkDraw():
        print("draw")
        break




