import turtle
import winsound

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Score
scoreA = 0
scoreB = 0


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=('Courier', 18, "bold"))

#Functions
def paddleA_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddleA_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddleB_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddleB_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard winding
win.listen()
win.onkeypress(paddleA_up, "w")
win.onkeypress(paddleA_down, "s")
win.onkeypress(paddleB_up, "Up")
win.onkeypress(paddleB_down, "Down")


#Mainloop
while True:
    win.update()

    #Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 
        winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
        winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)

    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1 
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=('Courier', 18, "bold"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1 
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=('Courier', 18, "bold"))


    #Paddle and Ball
    if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
        ball.dx *= -1
        
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
        ball.dx *= -1

    if scoreA >= 3:
        print("Player A won!")
        

    