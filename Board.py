class Board:
    def __init__(self):
        self.list = [str(i) for i in range(1, 10)]

    def DisplayBoard(self):
        for i in range (0,9,3):
            print(" | ".join(self.list[i:i+3]))
            if i<6:
                print("__"*5)

    def resetBoard(self):
        self.list=[str(i) for i in range(1,10)]

    def updateBoard(self,pos,sympol):
        if self.isValid(pos):
            self.list[pos-1]=sympol
            return True
        else: return False

    def isValid(self,position):
        return self.list[position -1].isnumeric()

    #cases of win
    #list[0]=list[1]=list[2] h
    #list[0]=list[3]=list[6] v
    #list[0]=list[4]=list[8] d

    #list[1]=list[4]=list[8] v

    #list[2]=list[5]=list[8] v
    #list[2]=list[4]=list[6] d

    #list[3]=list[4]=list[5] h
    #list[6]=list[7]=list[8] h
    def checkWin(self):
        win=False
        winCases=[
            [0,1,2],
            [0,3,6],
            [0,4,8],
            [1,4,7],
            [2,5,8],
            [2,4,6],
            [3,4,5],
            [6,7,8]]
        for sol in winCases:
            if(self.list[sol[0]]==self.list[sol[1]]
            ==self.list[sol[2]]):
                win=True
        return win







