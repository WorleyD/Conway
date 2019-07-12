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
            #print(row, cell)
            neighbours = lives(board, row, cell)
            if board[row][cell] == "o":
                if neighbours == 2 or neighbours == 3:
                    newboard[row][cell] = "o"
                else:
                    newboard[row][cell] = "_"
                    flag = True
            else:
                if neighbours == 3:
                    newboard[row][cell] = "o"
                    flag = True
                else:
                    newboard[row][cell] = "_"

    return newboard, flag

def seed():
    r = random.randint(1,400)
    return "o" if r % 3 == 0 else "_"
    
def initBoard():
    board = [[seed() for i in range(MAX)] for i in range(MAX)]
    return board

board = initBoard()
out = "#" * (MAX+2) + "\n"
for row in board:
    out +="#"
    for cell in row:
        out += cell
    out += "#\n"

out += "#" * (MAX+2) + "\n"
print(out)

layout = [[sg.Text(out, key='board', size=(30,30))]]
window = sg.Window("Welcome to Life", resizable=False).Layout(layout).Finalize()

while True:
    print("Life:")
    board, flag = update(board)
    sleep(1) 
    out = "#" * (MAX+2) + "\n"
    for row in board:
        out += "#"
        for cell in row:
            #print(cell, end="_")
            out += cell
        out += "#\n"
    out += "#" * (MAX+2) + "\n"
        
    event, values = window.Read(timeout=10)
    window.FindElement('board').Update(out)
    print(out)
