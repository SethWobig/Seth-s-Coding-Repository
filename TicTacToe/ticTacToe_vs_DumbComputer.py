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



    def checkWinCol(self,player):
        #check col
    
        if(self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] and self.board[0][0] == player):
            print("You won")
            self.win = True
        if(self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][0] == player):
            print("You won")
            self.win = True
        if(self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][0] == player):
            print("You won")
            self.win = True

        return self.win
        
    def checkWinRow(self,player):
        #check row
       
        if(self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[0][0] == player):
            print("You won")
            self.win = True
        if(self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[0][1] == player):
            print("You won")
            self.win = True
        if(self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[0][2] == player):
            print("You won")
            self.win = True

        return self.win

    def checkWinDiagonal(self,player):
            #check diagonal
        if(self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] == player):
            print("You won")
            self.win = True
        if(self.board[2][0] == self.board[1][1] and self.board[2][0] == self.board[0][2] and self.board[2][0] == player):
            print("You won")
            self.win = True

        return self.win

    def checkTie(self,player):
            #check tie
        tally = 0
        for i in self.board:
            for j in i:
                if(j == 0):
                    tally +=1
        if(tally == 0):
            print("Tie Game :(")
            self.win = True
            
        return self.win
            
    
        

    def play(self):
        #chooses which player starts
        rand = random.randint(0, 1)
        if rand == 1:
            player = 1
        else:
            player = 2

        while True:

            self.displayBoard()
            print()


            while True:
                #computer generated random point
                rowRand = random.randint(0,2)
                colRand = random.randint(0,2)

                if player == 1:
                    m,n = input("Player"+ str(player) +' please enter the coordinates for box (Ex. 0 0): ').split() #chose the position to mark
                    if(self.board[int(m)][int(n)] != 1 and self.board[int(m)][int(n)] != 2): #cannot enter an already taken position
                        break
                
                else:
                    m = str(rowRand)
                    n = str(colRand)
                    if(self.board[int(m)][int(n)] != 1 and self.board[int(m)][int(n)] != 2): #cannot enter an already taken position
                        print("The computer played: " + m +" " + n)
                        break
                
            self.board[int(m)][int(n)] = player
            

            if(self.checkWinCol(player)):
                break
            if(self.checkWinRow(player)):
                break
            if(self.checkWinDiagonal(player)):
                break
            if(self.checkTie(player)):
                break

            #switches players
            if player == 1:
                player = 2
            else:
                player = 1

            
        self.displayBoard()
        
    

ticTacToe().play()