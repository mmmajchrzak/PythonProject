import turtle

window = turtle.Screen()
window.title("PONG")
window.bgcolor("black")
window.setup(width=1000, height=600)
window.tracer(0)

# Wynik
score_l = 0
score_r = 0

# Lewa Paletka
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.shapesize(stretch_wid=6, stretch_len=0.5)
paddle_l.penup()
paddle_l.goto(-450, 0)
paddle_l.color("limegreen")

# Prawa Paletka
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.shapesize(stretch_wid=6, stretch_len=0.5)
paddle_r.penup()
paddle_r.goto(450, 0)
paddle_r.color("limegreen")

# Piłka
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.shapesize(stretch_wid=0.8, stretch_len=0.8)
ball.dx = 0.25
ball.dy = 0.25
ball.color("limegreen")

# Tablica Wyników
pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Player A:   0  -  Player B:   0", align="center", font=("Trebuchet MS", 28, "normal"))


# Fizyka Paletek
def paddle_l_up():
    y = paddle_l.ycor()
    y += 40
    paddle_l.sety(y)


def paddle_l_down():
    y = paddle_l.ycor()
    y -= 40
    paddle_l.sety(y)


def paddle_r_up():
    y = paddle_r.ycor()
    y += 40
    paddle_r.sety(y)


def paddle_r_down():
    y = paddle_r.ycor()
    y -= 40
    paddle_r.sety(y)


# Klawisze
window.listen()
window.onkeypress(paddle_l_up, "w")
window.onkeypress(paddle_l_down, "s")
window.onkeypress(paddle_r_up, "Up")
window.onkeypress(paddle_r_down, "Down")


# Main
while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bariery
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if paddle_r.ycor() > 235:
        paddle_r.sety(235)

    if paddle_r.ycor() < -235:
        paddle_r.sety(-235)

    if paddle_l.ycor() > 235:
        paddle_l.sety(235)

    if paddle_l.ycor() < -235:
        paddle_l.sety(-235)

    # Bariery

    if ball.xcor() > 450:
        score_l += 1
        pen.clear()
        pen.write("Player A:   {}  -  Player B:   {}".format(score_l, score_r), align="center",
                  font=("Trebuchet MS", 28, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -450:
        score_r += 1
        pen.clear()
        pen.write("Player A:   {}  -  Player B:   {}".format(score_l, score_r), align="center",
                  font=("Trebuchet MS", 28, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Kolizje

    if ball.xcor() < -435 and ball.ycor() < paddle_l.ycor() + 70 and ball.ycor() > paddle_l.ycor() - 70:
        ball.dx *= -1


    elif ball.xcor() > 435 and ball.ycor() < paddle_r.ycor() + 70 and ball.ycor() > paddle_r.ycor() - 70:
        ball.dx *= -1

    if ball.xcor() < -435 and ball.ycor() < paddle_l.ycor() + 70 and ball.ycor() > paddle_l.ycor() - 70:
        ball.color("red")


    elif ball.xcor() > 435 and ball.ycor() < paddle_r.ycor() + 70 and ball.ycor() > paddle_r.ycor() - 70:
        ball.color("blue")
