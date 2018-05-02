# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:27:36 2017

@author: skywalker
"""

import turtle
wn = turtle.Screen()
jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()

for size in range(12):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)
    jose.right(360/12)
    
wn.exitonclick()