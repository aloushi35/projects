#import the sockets library
import socket
#import class
from gameboard import BoardClass

#define the socket address and port
serverAddress= input('Enter an IP address:')
serverPort = int(input('Enter a port:'))

#connect to the server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Attempt to bind to server
serverSocket.bind((serverAddress,serverPort))

#listens for connections
serverSocket.listen(5)

#keeps track of connection
connectionCounter = 0

#accepts connections

clientSocket,clientAddress = serverSocket.accept()

print("Client connected from: ",clientAddress)

#Wait for message from player1
clientData = clientSocket.recv(1024)
print(clientData.decode())
playeruser = clientData.decode()
connectionCounter += 1

#send user to p1
p2user = input('Enter your username:')
sendtouser = clientSocket.send(p2user.encode())

def game():
    
    """ This function runs the tic tac toe game
    returns a functioning tic tac toe game
    """

    token = 'O'
    #creates an object personal to player2
    username = p2user
    playerusername = playeruser
    lastturn = p2user
    numbgames = 1
    wins = 0
    ties = 0
    losses = 0
    #tracks the count of moves
    count = 0
    g = BoardClass(username, playerusername, lastturn, numbgames, wins, ties, losses)
    #while loop
    try:
        while True:
            turn = 'X'
            #waits for message from p1
            print("Receiving...")
            clientData = clientSocket.recv(1024)
            g.updateGameBoard(clientData.decode(), turn)
            count += 1
            #checks for winner
            if count >= 5:
                if g.isWinner(count, token) == True:
                    clientData = clientSocket.recv(1024)
                    yesorno = clientData.decode()
                    #if no, end game
                    if yesorno == 'Fun Times':
                        print(yesorno)
                        g.printStats()
                        serverSocket.close()
                        break
                    #if yes, replay
                    if yesorno == 'Play Again':
                        print(yesorno)
                        g.resetGameBoard()
                        count = 0
                        continue
            #chekcs for tie
            if count >= 9:
                g.boardIsFull(count)
                clientData = clientSocket.recv(1024)
                yesorno = clientData.decode()
                #if no, end game
                if yesorno == 'Fun Times':
                    print(yesorno)
                    g.printStats()
                    serverSocket.close()
                    break
                #if yes, replay
                if yesorno == 'Play Again':
                    print(yesorno)
                    g.resetGameBoard()
                    count = 0
                    continue
                    

            turn = 'O'
            print(clientData.decode())
            #tells user where to place move
            print('Cooresponding Keys:')
            print('[1][2][3]')
            print('[4][5][6]')
            print('[7][8][9]')
            #takes p2 move
            move = input('Make your move[P2]? ')
            #updates game board for p2
            g.updateGameBoard(move, turn)
            count += 1
            #sends p2 move
            clientSocket.send(move.encode())

            turn = 'X'

            #checks for winner
            if count >= 5:
                if g.isWinner(count, token) == True:
                    clientData = clientSocket.recv(1024)
                    yesorno = clientData.decode()
                    #if no, end game
                    if yesorno == 'Fun Times':
                        print(yesorno)
                        g.printStats()
                        serverSocket.close()
                        break
                    #if yes, replay
                    if yesorno == 'Play Again':
                        print(yesorno)
                        g.resetGameBoard()
                        count = 0
                        continue

            

            
    except ValueError as e:
        print('ERROR', e)
    finally:
        #closing the connection when done
        serverSocket.close()

