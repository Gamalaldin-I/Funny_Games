from Menu import Menu
from Player import Player
from Board import Board


class Game:
    def __init__(self):
        self.player1=Player()
        self.player2=Player()
        self.players=[self.player1,self.player2]
        self.menu=Menu()
        self.board=Board()
        self.playerIndex=0
        #take the players data  names and sympols
    def getPlayers(self):
        for player in self.players:
            player.getPlayerData()

    def choosePos(self,sympol):
        #check if the input is not a char or string and between 1 and 10
        while True:
         pos=input("enter the new pos")
         if (pos.isdigit() and int(pos)in range(1,10)):
           break
        #update by the player symbol and the choosen position
        self.board.updateBoard(int(pos),sympol)
        #display this
        self.board.DisplayBoard()

    #display board and start playing
    def run_game(self):
        self.board.DisplayBoard()
        for i in range(1, 10):
            nowPlay = self.players[self.playerIndex]
            print(f"{nowPlay.name} should play")
            self.choosePos(nowPlay.sympol)
            if self.isWin():
                print(f"{nowPlay.name} won ")
                break
            self.switchTurn()
       #Start
    def start_game(self):
        if self.menu.startGame() == "1":
           self.getPlayers()
        else:
           print("good bye")
           return
        while True:
               self.run_game()
               if self.menu.endGame()=="1":
                self.board.resetBoard()
               else: break
     #to switch the turns
    def switchTurn(self):
        self.playerIndex=1-self.playerIndex

    def isWin(self):
        return self.board.checkWin()


game=Game()
game.start_game()
