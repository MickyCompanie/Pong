import turtle
import winsound
# pour linux et mac: import os

# wn: contraction pour le fenêtre (window)
wn = turtle.Screen()
wn.title("Pong par Micky Companie")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score

score1 = 0
score2 = 0

# Paddle1

paddle1 = turtle.Turtle()
# ce n'est pas la vitesse du mouvement du paddle mais la vitesse de son animation. (0) met l'animation au maximum de son animation
paddle1.speed(0)
# par défaut la shape fait 20px/20px
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

# Paddle2

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Fonctions

def paddle1Up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1Down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2Up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2Down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

# Keyboard binding

wn.listen()
wn.onkeypress(paddle1Up, "z")
wn.onkeypress(paddle1Down, "s")
wn.onkeypress(paddle2Up, "Up")
wn.onkeypress(paddle2Down, "Down")

# main game loop

while True:
        wn.update()

        # move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            # pour linux os.system("aplay bounce.wav&")
            # pour mac os.system("afplay bounce.wav&")
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            # pour linux os.system("aplay bounce.wav&")
            # pour mac os.system("afplay bounce.wav&")
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score1 += 1
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score2 +=1
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() -50):
            ball.setx(340)
            ball.dx *= -1
            # pour linux os.system("aplay bounce.wav&")
            # pour mac os.system("afplay bounce.wav&")
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() -50):
            ball.setx(-340)
            ball.dx *= -1
            # pour linux os.system("aplay bounce.wav&")
            # pour mac os.system("afplay bounce.wav&")
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)