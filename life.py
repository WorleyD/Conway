MAX = 10
import random
from time import sleep
import PySimpleGUI as sg

#almsot certainly a better way to do this
def lives(board, row, cell):
    neighbours = 0
    #first row (cant look up)
    if row == 0:
        #if we can look right, do it
        if cell != MAX-1:
            if board[row][cell+1] == "o":
                neighbours+=1
        #if we can look left, do it
        elif cell != 0:
            if board[row][cell-1] == "o":
                neighbours+=1
        #look down     
        if board[row+1][cell] == "o":
            neighbours+=1
            
    #last row (cant look down)        
    elif row == MAX -1:
        #if we can look right, do it
        if cell != MAX-1:
            if board[row][cell+1] == "o":
                neighbours+=1
        #if we can look left, do it
        elif cell == MAX-1:
            if board[row][cell-1] == "o":
                neighbours+=1
        #look up
        if board[row-1][cell] == "o":
            neighbours+=1
                
    #can look up or down
    else:
        #cant look left
        if cell != MAX-1:
            if board[row][cell+1] == "o":
                neighbours+=1
        #cant look right
        if cell != 0:
            if board[row][cell-1] == "o":
                neighbours+=1
        #look up and down
        if board[row+1][cell] == "o":
            neighbours+=1
        if board[row-1][cell] == "o":
            neighbours+=1   

    return neighbours


def update(board):
    newboard = [["_" for i in range(MAX)] for i in range(MAX)]
    for row in range(MAX):
        for cell in range(MAX):
            neighbours = lives(board, row, cell)
            if board[row][cell] == "o":
                if neighbours == 2 or neighbours == 3:
                    newboard[row][cell] = "o"
                else:
                    newboard[row][cell] = "_"
            else:
                if neighbours == 3:
                    newboard[row][cell] = "o"
                else:
                    newboard[row][cell] = "_"

    return newboard

def seed():
    r = random.randint(1,400)
    return "o" if r % 3 == 0 else "_"
    

board = [[seed() for i in range(MAX)] for i in range(MAX)]

out = ""
for row in board:
    for cell in row:
        #print(cell, end="_")
        out += cell + " "
    out += "\n"

print(out) 

window = sg.Window("Welcome to Life", resizable=False).Layout([[sg.Text(out, key='board')]]).Finalize()

while True:
    print("Life:")
    board = update(board)
    sleep(1) 
    out = ""
    for row in board:
        for cell in row:
            #print(cell, end="_")
            out += cell + " "
        out += "\n"
        
    event, values = window.Read(timeout=10)
    window.FindElement('board').Update(out)
    print(out)
