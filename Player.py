class Player:
    def __init__(self):
        self.name=""
        self.sympol=""

    def chooseName(self):
        while True:
            name=input("Enter your name only in alph ")
            if name.isalpha():
                self.name=name
                break
            else:
                print("invalid name try again")

    def chooseSympol(self):
        while True:
            sympol = input("Enter your Sympol only one char")
            if sympol.isalpha() and len(sympol)==1:
                self.sympol = sympol
                break
            else:
                print("invalid sympol try again")

    def getPlayerData(self):
        self.chooseName()
        self.chooseSympol()


