class BoardClass:

    def __init__(self, username, lastturn, wins, ties, losses):
        self.username = username
        self.lastturn = lastturn
        self.wins = int(wins)
        self.ties = int(ties)
        self.losses = int(losses)
        

    def updateGamesPlayed(self):
        return

    def resetGameBoard(self):
        restartgame = input("Play Again?")
        if restartgame == 'y' or restartgame == 'Y':
            for key in keyboard:
                board[key] = " "
                return

    def updateGameBoard(self):
        return(board['1'] + '|' + board['2'] + '|' + board['3'])
        return('-+-+-')
        return(board['4'] + '|' + board['5'] + '|' + board['6'])
        return('-+-+-')
        return(board['7'] + '|' + board['8'] + '|' + board['9'])
        

    def isWinner(self):
        if count >=5:
            if gameboard['1'] == gameboard['2'] == gameboard['3'] !=' ':
                print(gameboard)
                print(lasturn + 'Won!')
                self.wins += 1
                self.losses += 1
                return
            elif gameboard['4'] == gameboard['5'] == gameboard['5'] !=' ':
                print(gameboard)
                print('You Win!')
                self.wins += 1
                self.losses += 1
                return
            elif gameboard['7'] == gameboard['8'] == gameboard['9'] !=' ':
                print(gameboard)
                print('You Win!')
                self.wins += 1
                self.losses += 1
                return
            elif gameboard['1'] == gameboard['5'] == gameboard['9'] !=' ':
                print(gameboard)
                print('You Win!')
                self.wins += 1
                self.losses += 1
                return
            elif gameboard['3'] == gameboard['5'] == gameboard['7'] !=' ':
                print(gameboard)
                print('You Win!')
                self.wins += 1
                self.losses += 1
                return
            elif gameboard['1'] == gameboard['4'] == gameboard['7'] !=' ':
                print(gameboard)
                print('You Win!')
                self.wins += 1
                self.losses += 1
                return
            elif gameboard['2'] == gameboard['5'] == gameboard['8'] !=' ':
                print(gameboard)
                print('You Win!')
                self.wins += 1
                self.losses += 1
                return
            elif gameboard['3'] == gameboard['6'] == gameboard['9'] !=' ':
                print(gameboard)
                print('You Win!')
                self.wins += 1
                self.losses += 1
                return

    def boardIsFull(self):
        if count == 9:
            print("It's a Tie.")
            return

    def printStats(self):
        return

