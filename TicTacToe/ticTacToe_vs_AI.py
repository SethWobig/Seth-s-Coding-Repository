import random

class ticTacToe:

    def __init__(self):
        self.board = [0,0,0],[0,0,0],[0,0,0]
        self.prettyBoard = ['-','-','-'],['-','-','-'],['-','-','-']
        self.win = None

    def displayBoard(self):
        #converts 2d integer array into a string array, and displays it in a grid shape
        # 0 = '-'
        # 1 = 'X'
        # 2 = 'O'

        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == 1):
                    self.prettyBoard[i][j] = 'X'
                if(self.board[i][j] == 2):
                   self.prettyBoard[i][j] = 'O'

        for i in self.prettyBoard:
            for j in i:
                print(j, end = ' ')
            print()

    def checkWin(self,player):
        
        #check col
        win_state = [
        [self.board[0][0], self.board[0][1], self.board[0][2]],
        [self.board[1][0], self.board[1][1], self.board[1][2]],
        [self.board[2][0], self.board[2][1], self.board[2][2]],
        [self.board[0][0], self.board[1][0], self.board[2][0]],
        [self.board[0][1], self.board[1][1], self.board[2][1]],
        [self.board[0][2], self.board[1][2], self.board[2][2]],
        [self.board[0][0], self.board[1][1], self.board[2][2]],
        [self.board[2][0], self.board[1][1], self.board[0][2]],
    ]
        if [player, player, player] in win_state:
            return True
        else:
            return False
           
    def checkTie(self):
        self.win = True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    self.win = False
        return self.win

    def emptyCells(self):
        cells = []
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 0: #loops through the empty cells
                    cells.append([x, y])
        return cells


    def playMove(self, x, y, player):
        if self.board[x][y] == 0:
            self.board[x][y] = player
            return True
        else:
            return False

    def switchPlayer(self,player):
        if player == 1:
            player = 2
        elif player == 2:
            player = 1
        return player
        
    def minMax(self, depth, player):
            if player == 2: #computer/MAX
                best = [-1,-1,-100] #[best move row, best move col, best move value]
            else: #human/MIN
                best = [-1, -1, +100]
            
            if depth == 0 or self.checkWin(1) or self.checkWin(2): #checks if game ended
                if self.checkWin(2): #if comp wins
                    score = 1
                if self.checkWin(1): #if human wins
                    score = -1
                else:
                    score = 0
                return [-1,-1,score] 

            for cell in self.emptyCells():
                x, y = cell[0], cell[1]
                self.board[x][y] = player #assigns empty cell a mark
                score = self.minMax(depth - 1, self.switchPlayer(player)) #recursion 
                self.board[x][y] = 0
                score[0], score[1] = x, y

                if player == 2:
                    if score[2] > best[2]:
                        best = score #max value
                else:
                    if score[2] < best[2]:
                        best = score #min value
            
            return best

    def playerTurn(self, player):
        while True:
            x, y = [int(x) for x in input("Player"+ str(player) +' please enter the coordinates for box (Ex. 0 0): ').split()] #chose the position to mark
            if(self.board[x][y] != 1 and self.board[x][y] != 2): #cannot enter an already taken position
                break
        self.playMove(x,y,1)

    def compTurn(self):
        while True:
            rowRand = random.randint(0,2)
            colRand = random.randint(0,2) 
            x = str(rowRand)
            y = str(colRand)
            if(self.board[int(x)][int(y)] != 1 and self.board[int(x)][int(y)] != 2): #cannot enter an already taken position
                print(f"The computer played: {x}, {y}")
                break
        return int(x), int(y)

    def ai_turn(self,player):

        depth = len(self.emptyCells())
        if depth == 9:
            x = 0
            y = 0
        else:
            bestMove = self.minMax(depth, 2)
            x, y = bestMove[0], bestMove[1]
        
        self.playMove(x,y,2)



    def main(self):
        #chooses which player starts
        rand = random.randint(0, 1)
        if rand == 1:
            player = 1
        else:
            player = 2


        while True:

            self.displayBoard()
            print()

            if player == 1: #player choosing a move
                self.playerTurn(player)

            else: #computer choosing move
                self.ai_turn(player)
                     
            if(self.checkWin(1)):
                print("You beat the computer won")
                break
            if(self.checkWin(2)):
                print("The computer is better than you.")
                break
            if(self.checkTie()):
                print("tie game")
                break
            

            player = self.switchPlayer(player)
            
            
        self.displayBoard()
        
    
ticTacToe().main()