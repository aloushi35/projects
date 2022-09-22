#import the sockets library
import socket
#import class
from gameboard import BoardClass

import tkinter as tk

#print('Desktop Name:', socket.gethostname())

#define the server address
serverAddress = input('Enter an IP address:')
#define a server port
port = int(input('Enter a port:'))

#connect to server
connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#attemps to connect to server
connectionSocket.connect((serverAddress,port))


#takes the user from p1 and sends it to p2
nameuser = input('Enter your username:')
senduser = connectionSocket.send(nameuser.encode())

#receives user from p2
serverData = connectionSocket.recv(1024)
print(serverData.decode())
playeruser = serverData.decode()

def game():

    """ This function runs the tic tac toe game

    returns a functioning tic tac toe game
    
    """
    #tracks the count of moves
    count = 0

    token = 'X'
    
    #creates an object personal to player1
    username = nameuser
    playerusername = playeruser
    lastturn = nameuser
    numbgames = 1
    wins = 0
    ties = 0
    losses = 0

    g = BoardClass(username, playerusername, lastturn, numbgames, wins, ties, losses)

    #whileloop
    try:
        while True:
           turn = 'X'
           #lets user know where to place move
           print('Cooresponding Keys:')
           print('[1][2][3]')
           print('[4][5][6]')
           print('[7][8][9]')
           #takes move from p1
           move = input('make your move [P1]? ')
           #updates the gameboard
           g.updateGameBoard(move, turn)
           #sends the move to p2
           connectionSocket.send(move.encode())
           #increases the count of moves by 1
           count += 1

           #checks if there is a winner
           if count >= 5:
               if g.isWinner(count, token) == True:
                  playagain = input('Do you want to play again?')
                   #if yes, then restarts game
                  if playagain == 'y' or playagain == 'Y':
                      replay = 'Play Again'
                      connectionSocket.send(replay.encode())
                      g.resetGameBoard()
                      count = 0
                      continue
                      #if no, then ends game for both players
                  if playagain == 'N' or playagain == 'n' :
                      salute = 'Fun Times'
                      connectionSocket.send(salute.encode())
                      g.printStats()
                      connectionSocket.close()
                      break 
               
           #checks if there is a tie
           if count >= 9:
               g.boardIsFull(count)
               #asks user if they want to replay
               playagain = input('Do you want to play again?')
               #if yes, then restarts game
               if playagain == 'y' or playagain == 'Y':
                   replay = 'Play Again'
                   connectionSocket.send(replay.encode())
                   g.resetGameBoard()
                   count = 0
                   continue
                   #hiddenlineofcodethatdoesnothing
                #if no, then ends game for both players
               if playagain == 'N' or playagain == 'n' :
                   salute = 'Fun Times'
                   connectionSocket.send(salute.encode())
                   g.printStats()
                   connectionSocket.close()
                   break
           #changes turn to O to record p2 move
           turn = 'O'
           #receive's p2 move
           serverData = connectionSocket.recv(1024)
           g.updateGameBoard(serverData.decode(), turn)
           turn = 'X'
           #updates gameboard for p1
           print(serverData.decode())
           g.updateGameBoard(move, turn)
           count += 1

           #checks if there is a winner
           if count >= 5:
               if g.isWinner(count, token) == True:
                  playagain = input('Do you want to play again?')
                   #if yes, then restarts game
                  if playagain == 'y' or playagain == 'Y':
                      replay = 'Play Again'
                      connectionSocket.send(replay.encode())
                      g.resetGameBoard()
                      count = 0
                      continue
                      #if no, then ends game for both players
                  if playagain == 'N' or playagain == 'n' :
                      salute = 'Fun Times'
                      connectionSocket.send(salute.encode())
                      g.printStats()
                      connectionSocket.close()
                      break
           
    except ValueError as e:
        print('Error', e)
    finally:
        connectionSocket.close()

        #connectionrefusederror exception
    
