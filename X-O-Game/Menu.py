class Menu:
    def startGame(self):
        print("Hello to X O")
        print("1:Start the game")
        print("2:End the game")
        choise= input("Enter your choise 1 or 2")
        return choise
    def endGame(self):
        text="""
        Game Over 
        1 . Restart the Game 
        2 . End game
        Enter your choise 1 or 2 : """
        choise=input(text)
        return choise
