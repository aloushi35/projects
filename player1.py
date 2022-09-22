#import the sockets library
import socket
#import class
from gameboard import BoardClass
from tkinter import *
from _thread import *
from functools import partial

#print('Desktop Name:', socket.gethostname())

#define the server address
serverAddress = '127.0.0.1'
#define a server port
port = 8007


connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#attemps to connect to server
connectionSocket.connect((serverAddress,port))

tk = Tk()
tk.title("Tic-Tac-Toe")

token = 'X'
    
#creates an object personal to player1
playertoken = Label(tk, text="Player(X)").grid()
user = StringVar()
userlabel = Label(tk, text="Enter a username").grid()
usertext = Entry(tk, text=user).grid()
buttonusername = Button(tk, text="Submit Username",command=lambda:setText()).grid()
def setText():
    global user
    global usernameUI
    global g
    usernameUI = user.get()
    username = usernameUI
    playerusername = 'playeruser'
    lastturn = 'nameuser'
    numbgames = 1
    wins = 0
    ties = 0
    losses = 0
    g = BoardClass(username, playerusername, lastturn, numbgames, wins, ties, losses)
turn = 'X'
myturn = 1
def updateGUI(button, i, j):
    global myturn
    global connectionSocket
    global token
    turn = 'X'
    if (button["text"]==" " and myturn == 1):
        button["text"]=token
        buttonnumber = i*3+j
        connectionSocket.send(str(buttonnumber).encode('utf-8'))
        myturn = 0
        move = '7'
        g.updateGameBoard(move,turn)
        checkWinner(button)

counter = 1
def checkWinner(button):
    global token
    global buttons
    global counter
    win = 0
    count = 0
    for i in range(3):
        if ((buttons[i][0]["text"]==buttons[i][1]["text"] and buttons[i][0]["text"]==buttons[i][2]["text"] and buttons[i][0]["text"]!=" ")
        or (buttons[0][i]["text"]==buttons[1][i]["text"] and buttons[0][i]["text"]==buttons[2][i]["text"] and buttons[0][i]["text"]!=" ")):
            if(button["text"] == token):
                winner = Label(tk, text="You Win!").grid()
                g.isWinner(count, token)
                g.wins += 1
            else:
                loser = Label(tk, text="You Lose.").grid()
                g.isWinner(count, token)
                g.losses += 1
            win = 1
            yesorno()
    if win == 0:
        if ((buttons[0][0]["text"]==buttons[1][1]["text"] and buttons[0][0]["text"]==buttons[2][2]["text"] and buttons[0][0]["text"]!=" ")
        or (buttons[0][2]["text"]==buttons[1][1]["text"] and buttons[0][2]["text"]==buttons[2][0]["text"] and buttons[0][2]["text"]!=" ")):
            if(button["text"] == token):
                winner = Label(tk, text="You Win!").grid()
                g.isWinner(count, token)
                g.wins +=1
            else:
                loser = Label(tk, text="You Lose.").grid()
                g.isWinner(count, token)
                g.losses += 1
            win == 1
            yesorno()
    if win == 0 and counter == 9:
        tie = Label(tk, text="It's a Tie").grid()
        g.boardIsFull(count)
        g.ties += 1
        yesorno()
    counter = counter+1

def yesorno():
    global counter
    global myturn
    global buttons
    global tk
    playagain = Label(tk, text = "Do you want to play again?").grid()
    yes = Button(tk, text='Yes')
    yes.config(command=partial(reset))
    yes.grid()
    noplay = Button(tk, text='No')
    noplay.config(command=partial(finish))
    noplay.grid()
    stats()

def reset():
    global counter
    global myturn
    global buttons
    yes = 'Yes'
    connectionSocket.send(yes.encode('utf-8'))
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ")
    myturn = 1
    counter = 0

def finish():
    no = 'No'
    connectionSocket.send(no.encode('utf-8'))
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
def recvMove(connectionSocket):
    global buttons
    global myturn
    while True:
        buttonnumber = int(connectionSocket.recv(1024).decode('utf-8'))
        row = int(buttonnumber/3)
        column = int(buttonnumber%3)
        buttons[row][column]['text'] = 'O'
        myturn = 1
        checkWinner(buttons[row][column])
start_new_thread(recvMove, (connectionSocket,))
tk.mainloop()
    
