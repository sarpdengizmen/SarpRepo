# PONG BASE GAME 
# YERLIZEKA

import turtle
import random
import platform
import os

# Platform Check
platform = platform.system()
#get path of the file
path = os.path.dirname(os.path.abspath(__file__))
if platform == "Windows":
    import winsound
#change directory to the file path
os.chdir(path)

def playsound(soundfile, platform):
    if platform == "Windows":
        winsound.PlaySound(soundfile, winsound.SND_ASYNC)
    elif platform == "Linux":
        os.system(f"aplay -q {soundfile}&")
    elif platform == "Darwin":
        os.system(f"afplay {soundfile}&")
    else:
        print("Platform not supported")
    

color_array = ["black", "white"]

# Window Setup
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor(color_array[0])
window.setup(width=800, height=600)
window.tracer(0) # window update miktari ayari 0 = max hiz bekleme yok

# P1 Paddle
P1_Paddle = turtle.Turtle() # turtle object
P1_Paddle.speed(0) # animation speed 
P1_Paddle.shape("square") # paddle shape
P1_Paddle.color(color_array[1]) # paddle color
P1_Paddle.shapesize(stretch_wid=5, stretch_len=1) # paddle size 5x20px 1x20px
P1_Paddle.penup() # disable line drawing
P1_Paddle.goto(-350, 0) # paddle starting position

# P2 Paddle
P2_Paddle = turtle.Turtle() # turtle object
P2_Paddle.speed(0) # animation speed 
P2_Paddle.shape("square") # paddle shape
P2_Paddle.color(color_array[1]) # paddle color
P2_Paddle.shapesize(stretch_wid=5, stretch_len=1) # paddle size 5x20px 1x20px
P2_Paddle.penup() # disable line drawing
P2_Paddle.goto(350, 0) # paddle starting position

# Ball
Ball = turtle.Turtle() # turtle object
Ball.speed(0) # animation speed
Ball.shape("square") # ball shape
Ball.color(color_array[1]) # ball color
Ball.penup() # disable line drawing
Ball.goto(0, 0) # ball starting position

#Ball movement increments (depending on computer speed may need to be adjusted)
diff = 0.2 # ball movement speed
Ball.dx = diff
Ball.dy = diff

# Score
P1_Score = 0
P1_Old=0
P2_Score = 0
P2_Old=0

# Scoreboard
Scoreboard = turtle.Turtle() # turtle object
Scoreboard.speed(0) # animation speed
Scoreboard.color(color_array[1]) # scoreboard color
Scoreboard.penup() # disable line drawing
Scoreboard.hideturtle() # hide turtle
Scoreboard.goto(0, 260) # scoreboard starting position
Scoreboard.write(f"P1: {P1_Score}                  P2: {P2_Score}", align="center", font=("Courier", 24, "bold")) # scoreboard text

# Scoreboard Update Function
def Scoreboard_Update():
    Scoreboard.clear()
    Scoreboard.write(f"P1: {P1_Score}                  P2: {P2_Score}", align="center", font=("Courier", 24, "bold")) # scoreboard text

paddleincrement = 40
# Movement Functions
def P1_Paddle_Up():
    y = P1_Paddle.ycor() # get y coordinate
    if y > 250:
        return 
    y += paddleincrement # add 20px
    P1_Paddle.sety(y) # set y coordinate

def P1_Paddle_Down():
    y = P1_Paddle.ycor() # get y coordinate
    if y < -250:
        return
    y -= paddleincrement # add 20px
    P1_Paddle.sety(y) # set y coordinate

def P2_Paddle_Up():
    y = P2_Paddle.ycor() # get y coordinate
    if y > 250:
        return
    y += paddleincrement # add 20px
    P2_Paddle.sety(y) # set y coordinate

def P2_Paddle_Down():
    y = P2_Paddle.ycor() # get y coordinate
    if y < -250:
        return
    y -= paddleincrement # add 20px
    P2_Paddle.sety(y) # set y coordinate

# Keyboard Binding
window.listen() # listen keyboard inputs
window.onkeypress(P1_Paddle_Up, "w") # w key for P1_Paddle_Up
window.onkeypress(P1_Paddle_Down, "s") # s key for P1_Paddle_Down
window.onkeypress(P2_Paddle_Up, "Up") # Up key for P2_Paddle_Up
window.onkeypress(P2_Paddle_Down, "Down") # Down key for P2_Paddle_Down

Anim_Counter = 0
def Recolor(colorarray):
    P1_Paddle.color(colorarray[1])
    P2_Paddle.color(colorarray[1])
    window.update()
    return

def spacekey():
    global P1_Score
    global P2_Score
    global P1_Old
    global P2_Old
    global Scoreboard
    global Ball
    global reset
    P1_Score = 0
    P2_Score = 0
    P1_Old = 0
    P2_Old = 0
    Scoreboard_Update()
    P1_Paddle.goto(-350, 0)
    P2_Paddle.goto(350, 0)
    Scoreboard.clear()
    Scoreboard.goto(0, 260)
    Ball.showturtle()
    Ball.goto(0, 0)
    reset = True
    Scoreboard.write(f"P1: {P1_Score}                  P2: {P2_Score}", align="center", font=("Courier", 24, "bold"))

# Main Game Loop
while True:
    window.update() # window update
    if P1_Score == 5 or P2_Score == 5: # Game Over
        playsound("gameover.wav", platform)
        Ball.hideturtle()
        Scoreboard.clear()
        Scoreboard.goto(0, 0)
        Scoreboard.write("GAME OVER!", align="center", font=("Courier", 24, "bold"))
        Scoreboard.goto(0, -50)
        Scoreboard.write("Esc to exit", align="center", font=("Courier", 24, "bold"))
        Scoreboard.goto(0, -100)
        Scoreboard.write("Space to restart", align="center", font=("Courier", 24, "bold"))
        window.update()
        window.onkeypress(window.bye, "Escape") # Escape key for exit
        window.onkeypress(spacekey, "space")
        reset = False
        while not(reset):
            window.update()
            pass
        window.onkeypress(None, "Escape") # Escape key for exit
        window.onkeypress(None, "space")
    
    if P1_Score != P1_Old or P2_Score != P2_Old: #Score animation
        P1_Old=P1_Score
        P2_Old=P2_Score
        window.tracer(1,30)   # Slowdown refresh rate
        while Anim_Counter < 4:
            color_array = color_array[::-1] # reverse color array
            Anim_Counter += 1
            Recolor(color_array) 
        Anim_Counter = 0
        window.tracer(0)

    # Ball Movement
    Ball.setx(Ball.xcor() + Ball.dx) # ball movement
    Ball.sety(Ball.ycor() + Ball.dy) # ball movement

    # Border Checking
    if Ball.ycor() > 290: # top border !ball height = 20px
        playsound("bounce.wav", platform)
        Ball.sety(290)
        Ball.dy *= -1 # reverse direction
    
    if Ball.ycor() < -290: # bottom border
        playsound("bounce.wav", platform)
        Ball.sety(-290)
        Ball.dy *= -1 # reverse direction

    # Paddle and Ball Collisions
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < P2_Paddle.ycor() + 40 and Ball.ycor() > P2_Paddle.ycor() - 40):
        playsound("bounce.wav", platform)
        Ball.setx(340)
        Ball.dx *= -1
    
    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < P1_Paddle.ycor() + 40 and Ball.ycor() > P1_Paddle.ycor() - 40):
        playsound("bounce.wav", platform)
        Ball.setx(-340)
        Ball.dx *= -1
    
    # Score
    if Ball.xcor() > 390:
        playsound("score.wav", platform)
        P1_Paddle.goto(-350, 0)
        P2_Paddle.goto(350, 0)
        Ball.goto(0, 0)
        Ball.dx *= -1
        Ball.dy *= random.choice([-1,1])
        P1_Old=P1_Score
        P1_Score += 1
        Scoreboard_Update()
    
    if Ball.xcor() < -390:
        playsound("score.wav", platform)
        P1_Paddle.goto(-350, 0)
        P2_Paddle.goto(350, 0)
        Ball.goto(0, 0)
        Ball.dx *= -1
        Ball.dy *= random.choice([-1,1])
        P2_Old=P2_Score
        P2_Score += 1
        Scoreboard_Update()
    



    



