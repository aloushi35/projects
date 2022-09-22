#import the sockets library
import socket
#import class
from gameboard import BoardClass
from tkinter import *
from _thread import *
from functools import partial

#define the socket address and port
serverAddress= '127.0.0.1'
serverPort = 8007

#connect to the server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Attempt to bind to server
serverSocket.bind((serverAddress,serverPort))

#listens for connections
serverSocket.listen(5)

#accepts connections

clientSocket,clientAddress = serverSocket.accept()

tk = Tk()
tk.title("Tic-Tac-Toe")
playertoken = Label(tk, text="Player(O)").grid()
username = 'player2'
playerusername = 'playeruser'
lastturn = 'player2'
numbgames = 1
wins = 0
ties = 0
losses = 0
g = BoardClass(username, playerusername, lastturn, numbgames, wins, ties, losses)
myturn = 0
token = 'O'

def updateGUI(button, i, j):
    global myturn
    global clientSocket
    global token
    turn = 'O'
    if (button["text"]==" " and myturn == 1):
        button["text"]=token
        buttonnumber = i*3+j
        clientSocket.send(str(buttonnumber).encode('utf-8'))
        move = '7'
        g.updateGameBoard(move,turn)
        myturn = 0
        checkWinner(button)
counter = 1
def checkWinner(button):
    global token
    global buttons
    global counter
    global tk
    win = 0
    count = 0
    for i in range(3):
        if ((buttons[i][0]["text"]==buttons[i][1]["text"] and buttons[i][0]["text"]==buttons[i][2]["text"] and buttons[i][0]["text"]!=" ")
        or (buttons[0][i]["text"]==buttons[1][i]["text"] and buttons[0][i]["text"]==buttons[2][i]["text"] and buttons[0][i]["text"]!=" ")):
            if(button["text"] == token):
                winner = Label(tk, text="You Win!").grid()
                g.isWinner(count, token)
                g.wins += 1
                stats()
            else:
                loser = Label(tk, text="You Lose.").grid()
                g.isWinner(count, token)
                g.losses +=1
                stats()
            win = 1
            reset()
    if win == 0:
        if ((buttons[0][0]["text"]==buttons[1][1]["text"] and buttons[0][0]["text"]==buttons[2][2]["text"] and buttons[0][0]["text"]!=" ")
        or (buttons[0][2]["text"]==buttons[1][1]["text"] and buttons[0][2]["text"]==buttons[2][0]["text"] and buttons[0][2]["text"]!=" ")):
            if(button["text"] == token):
                winner = Label(tk, text="You Win!").grid()
                g.isWinner(count, token)
                g.losses += 1
                stats()
            else:
                loser = Label(tk, text="You Lose.").grid()
                g.isWinner(count, token)
                g.losses += 1
                stats()
            win == 1
            reset()
    if win == 0 and counter == 9:
        tie = Label(tk, text="It's a Tie").grid()
        g.ties += 1
        g.boardIsFull(count)
        stats()
        reset()
    counter = counter+1

def reset():
    global counter
    global myturn
    global buttons
    response = clientSocket.recv(1024).decode('utf-8')
    if response == 'Yes':
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(text=" ")
        myturn = 0
        counter = 0
    if response == 'No':
        tk.destroy()

def stats():
    usernameofp2 = g.username
    numbofwins = g.wins
    numboflosses = g.losses
    numbofties = g.ties
    numbofgame = g.numbgames
    gameuser = Label(tk, text=usernameofp2).grid()
    gamenumb = Label(tk, text=numbofgame).grid()
    gamewins = Label(tk, text=numbofwins).grid()
    gamelosses = Label(tk, text=numboflosses).grid()
    gameties = Label(tk, text=numbofties).grid()

buttons = [[0 for x in range(3)] for y in range (3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(tk,text=" ",height=4,width=8,bg="black",activebackground="white",fg="black",font="Times 15 bold")
        buttons[i][j].config(command=partial(updateGUI, buttons[i][j], i, j))
        buttons[i][j].grid(row=i+10, column=j+3)

def recvMove(clientSocket):
    global buttons
    global myturn
    while True:
        buttonnumber = int(clientSocket.recv(1024).decode('utf-8'))
        row = int(buttonnumber/3)
        column = int(buttonnumber%3)
        buttons[row][column]['text'] = 'X'
        myturn = 1
        checkWinner(buttons[row][column])
start_new_thread(recvMove, (clientSocket,))
tk.mainloop()
   

