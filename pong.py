import turtle

# wn pour window
wn = turtle.Screen()
wn.title("Pong par Micky Companie")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle1

paddle1 = turtle.Turtle()
# ce n'est pas la vitesse du paddle en soit, mais la vitesse de son animation (0) met l'animation au maximum de son animation
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