class Player:
    def __init__(self):
        #attriputes
        self.name=""
        self.sympol=""

    def chooseName(self):
        #Enter the name in alpha only
        while True:
            name=input("Enter your name only in alpha ")
            if name.isalpha():
                self.name=name
                break
            else:
                print("invalid name try again")
      
    def chooseSympol(self):
        #Enter the sympol only by one char
        while True:
            sympol = input("Enter your Sympol only one char")
            if sympol.isalpha() and len(sympol)==1:
                self.sympol = sympol
                break
            else:
                print("invalid sympol try again")
     #get player data
    def getPlayerData(self):
        self.chooseName()
        self.chooseSympol()


