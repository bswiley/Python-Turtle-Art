#!/usr/bin/env python3
from turtle import Turtle, Screen
import random
SPEED = 0
FMIN = 40
FMAX = 100
PENWIDTH = 60
STEPS = 32000
ts = []
W = 16000
H = 9000
LX = W/2/-1
LX = int(LX)
HX = W/2
HX = int(HX)
LY = H/2/-1
LY = int(LY)
HY = H/2
HY = int(HY)
MHX = W/4
MHX = int(MHX)
MHY = H/4
MHY = int(MHY)
MLX = W/2/-1
MLX =int (MLX)
MLY = H/2/-1
MLY = int(MLY)
LHX = MHX/2
LHX = int(LHX)
LLX = MLX/2
LLX = int(LLX)
LLY = MLY/2
LLY = int(LLY)
LHY = MHY/2
LHY =int(LHY)
START = [0,0, LX,LY, HX,HY, LX,HY, HX,LY, MHX,MHY, MHX,MLY, MLX,MLY, MLX,MHY, LHX,LHY, LHX,LLY, LLX,LLY, LLX,LHY]
CL = [10,10,10,10,10,10,10,10,10,10,10,10,10,10]
CH = [240,240,240,255,255,255,240,240,240,255,255,240,240,240]
print (START)
on = True
screen = Screen()
screen.colormode(255)
screen.setup(width=1.0, height=1.0)
screen.screensize(W,H)
screen.bgcolor(204,255,255)
screen.tracer(0)
for u in range (int(len(START)/2-1)):
    t = Turtle()
    t.pensize (PENWIDTH)
    t.hideturtle()
    t.speed(SPEED)
    t.color(145,90,25)
    t.seth(450)
    t.penup()
    t.goto(START[u*2], START[u*2+1])
    t.pendown()
    ts.append(t)

a = 30

for s in range (STEPS):
    print (s)
    for v in range (int(len(START)/2-1)):
        d = random.randint(1,100)
        if ts[v].ycor() > HY and ts[v].xcor() > HX:
            a = random.randint(180,270)
            ts[v].setheading(a)
        elif ts[v].ycor() < LY and ts[v].xcor() < LX:
            a = random.randint(0,90)
            ts[v].setheading(a)
        elif ts[v].ycor() > HY and ts[v].xcor() > LX:
            a = random.randint(270,360)
            ts[v].setheading(a)
        elif ts[v].ycor() < LY and ts[v].xcor() > HX:
            a = random.randint(90, 180)
            ts[v].setheading(a)
        elif ts[v].ycor() > HY:
            a = random.randint(180,360)
            ts[v].setheading(a)
        elif ts[v].ycor() < LY:
            a = random.randint(0,180)
            ts[v].setheading(a)
        elif ts[v].xcor() > HX:
            a = random.randint(90,270)
            ts[v].setheading(a)
        elif ts[v].xcor() < LX:
            a = random.randint(270,450)
            ts[v].setheading(a)
        elif d < 30:
            a = random.randint (0,359)
            ts[v].setheading(a)

        r = random.randint(CL[v],CH[v])
        g = random.randint(CL[v],CH[v])
        b = random.randint(CL[v],CH[v])
        ts[v].color(r,g,b)
        ts[v].forward(random.randint(FMIN,FMAX))

screen.update() # Ensure all drawing is rendered
canvas = screen.getcanvas()

canvas.postscript(
    file="art.eps",
    x=-W/2,
    y=-H/2,
    width=W,
    height=H,
    pagewidth=W,
    pageheight=H
)
screen.exitonclick()

