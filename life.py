MAX = 20
import random
from time import sleep
import PySimpleGUI as sg

def lives(board, row, cell):
    neighbours = 0
    #first row (cant look North)
    if row == 0:
        #if we can look East, do it
        if cell != MAX-1:
            if board[row][cell+1] == "o":       #East
                neighbours+=1
            if board[row+1][cell+1] == "o":     #SouthEast
                neighbours+=1
        #if we can look West, do it
        if cell != 0:
            if board[row][cell-1] == "o":       #West
                neighbours+=1
            if board[row+1][cell-1] == "o":     #SouthWest
                neighbours +=1
        #look South     
        if board[row+1][cell] == "o":       
            neighbours+=1

        #print(row, ",", cell, " has ",neighbours," neighbours")
        
    #last row (cant look South)        
    elif row == MAX -1:
        #if we can look East, do it
        if cell != MAX-1:
            if board[row][cell+1] == "o":       #East
                neighbours+=1
            if board[row-1][cell+1] == "o":     #NorthEast
                neighbours+=1
        #if we can look West, do it
        if cell == MAX-1:
            if board[row][cell-1] == "o":       #West
                neighbours+=1
            if board[row-1][cell-1] == "o":     #NorthWest
                neighbours +=1
        #look North
        if board[row-1][cell] == "o":           
            neighbours+=1
                
    #can look North or South
    else:
        #cant look West
        if cell != MAX-1:
            if board[row][cell+1] == "o":       #East
                neighbours+=1
            if board[row+1][cell+1] == "o":     #SouthEast
                neighbours += 1
            if board[row-1][cell+1] == "o":     #NorthEast
                neighbours+=1
        #cant look East
        if cell != 0:
            if board[row][cell-1] == "o":       #West 
                neighbours+=1
            if board[row+1][cell-1] == "o":     #SouthWest
                neighbours +=1
            if board[row-1][cell-1] == "o":     #NorthWest
                neighbours +=1
        
        if board[row+1][cell] == "o":           #South
            neighbours+=1
        if board[row-1][cell] == "o":           #North
            neighbours+=1   

    return neighbours


def update(board):
    newboard = [["_" for i in range(MAX)] for i in range(MAX)]
    flag = False
    for row in range(0,MAX):
        for cell in range(0,MAX):
            #get neighbour count for each cell
            neighbours = lives(board, row, cell)
            
            #update live cell
            if board[row][cell] == "o":
                if neighbours == 2 or neighbours == 3:
                    newboard[row][cell] = "o"
                else:
                    newboard[row][cell] = "_"
                    flag = True
            #update dead cell
            else:
                if neighbours == 3:
                    newboard[row][cell] = "o"
                    flag = True
                else:
                    newboard[row][cell] = "_"

    return newboard, flag

def seed():
    #random boring seeding
    r = random.randint(1,400)
    return "o" if r % 6 == 0 else "_"
    
def initBoard():
    #seed each cell to save new random board
    board = [[seed() for i in range(MAX)] for i in range(MAX)]
    return board

#create board
board = initBoard()

#get board plus border as string
out = "#" * (MAX+2) + "\n"
for row in board:
    out +="#"
    for cell in row:
        out += cell
    out += "#\n"

out += "#" * (MAX+2) + "\n"

#create gui window
layout = [[sg.Text("Simulation starting:", key='topText', size=(20,2))],[sg.Text(out, key='board')], [sg.Button("Reset")]]
window = sg.Window("Life", resizable=False).Layout(layout)

while True:
    #get next board generation
    board, flag = update(board)
    sleep(1) 
    #update board string for gui
    out = "#" * (MAX+2) + "\n"
    for row in board:
        out += "#"
        for cell in row:
            out += cell
        out += "#\n"
    out += "#" * (MAX+2) + "\n"
    
    #check for button press
    event, values = window.Read(timeout=10)
    
    #flag tracks if new board is equal to old board
    if not flag:
        #prepare to reset if so
        window.FindElement('topText').Update("Simulation has stabilized. Restarting...")
        window.Refresh()
    #if reset button was pushed    
    if event == "Reset":
        #prepare
        window.FindElement('topText').Update("Restarting...")
        window.Refresh()
    
    #reset board
    if event == "Reset" or not flag:
        sleep(3)
        board = initBoard()
        
    #update window    
    window.FindElement('topText').Update("Simulation running...")
    window.FindElement('board').Update(out)
