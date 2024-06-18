import turtle

score1=0
score2=0
goal=10
winner=""
x=0

#screen
#initialize the screen
wind=turtle.Screen()
#set the title of screen
wind.title("ping pong game by gamal hataba")
#set background color
wind.bgcolor("black")
#set the width and hieght to the screen
wind.setup(width=800,height=600)
#the speed of the screen updating
wind.tracer(1)

#madrab 1
#initialize the madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.penup()
#its size every one stretch represent 20px
madrab1.shapesize(stretch_wid=5,stretch_len=1)
#the position
madrab1.goto(-350,0)

#make madrab2 by the same way of madrab1
#madrab 2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("green")
madrab2.penup()
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.goto(350,0)

#by the same way make the ball
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
#the dimention of x and y axis when ball begin to move
ball.dx=2.5
ball.dy=2.5

#score

score=turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.goto(0,250)
score.hideturtle()
score.write("Gamal : 0 || Kareem : 0 ",align="center",font=("Ariel",24,"normal"))

#moves of madrab1
def madrab1Up():
    #get y value of madrab1
    y=madrab1.ycor()
    #increase this value by 20px
    y= y+ 20
    #reset by the new value
    madrab1.sety(y)
    
def madrab1down():
    y=madrab1.ycor()
    #decrease by 20 px
    y= y- 20
    madrab1.sety(y)
    
#moves of madrab2
def madrab2Up():
    y=madrab2.ycor()
    y= y+ 20
    madrab2.sety(y)
def madrab2down():
    y=madrab2.ycor()
    y= y- 20
    madrab2.sety(y)
    
#keybord controls
wind.listen()    #to make the screen expect an input form the keybord
#when press w button move madrab1 up
wind.onkeypress(madrab1Up,"w") 
#when press s button move madrab1 down
wind.onkeypress(madrab1down,"s")
#when press Up button move madrab2 up
wind.onkeypress(madrab2Up,"Up")
#when press Down button move madrab2 down
wind.onkeypress(madrab2down,"Down")


while x==0 :
    #update the screen every iterration
    wind.update()
    #moving the ball
    ball.setx (ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

#border check up and down
    if ball.ycor()==290:
        ball.dy*=-1
    if ball.ycor()==-290:
        ball.dy*=-1

#case player1 miss the ball
    if (ball.xcor()==-400) : # the ball out the side of madrab1 
        ball.goto(0,0)  #return the ball to the first position 
        ball.dx*=-1     #reverse the x dimintion of the ball
        score2+=1       #increase the score of player2
        score.clear()   #clear the previosc score to write the new score
        score.write("Gamal : {} || Kareem : {} ".format(score1,score2),align="center",font=("Ariel",24,"normal"))
#case the player2 miss the ball    
    if (ball.xcor()==400) :
        ball.goto(0,0)
        ball.dx*=-1
        score1+=1
        score.clear()
        score.write("Gamal : {} || Kareem : {} ".format(score1,score2),align="center",font=("Ariel",24,"normal"))
#case the madrab2 catch the ball
    if (ball.xcor() >340 and ball.xcor()< 350) and (ball.ycor() < madrab2.ycor()+40 and ball.ycor()>madrab2.ycor()-40) :
        ball.setx(340)
        ball.dx*=-1
#case the madrab1 catch the ball
    if (ball.xcor() <-340 and ball.xcor()> -350) and (ball.ycor() < madrab1.ycor()+40 and ball.ycor()>madrab1.ycor()-40) :
        ball.setx(-340)
        ball.dx*=-1
    
    #if(score1==goal):
        #score.clear()
        #  score.color("red")
        # score.goto(0,0)
        #score.write("Gamal won",align="center",font=("Ariel",70,"normal"))
        #winner="Gamal"
        #x=-1
        #if(score2==goal):
        #  score.clear()
        # score.color("blue")
        #score.goto(0,0)
        #score.write("Kareem won",align="center",font=("Ariel",70,"normal"))
        #winner="Kareem"
    
 
#score

    
