import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
print("Enter the Value of X1: ")
x1 = int(input())
print("Enter the Value of X2: ")
x2 = int(input())
print("Enter the Value of Y1: ")
y1 = int(input())
print("Enter the Value of Y2: ")
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

if abs(dx) > abs(dy):
    steps = abs(dx)
else:
    steps = abs(dy)

xincrement = dx/steps
yincrement = dy/steps

i = 0

xcoordinates = []
ycoordinates = []


while i < steps:
    i +=1
    x1 = x1 + xincrement
    y1 = y1 + yincrement
    print(f"X = {x1}, Y = {y1}")
    xcoordinates.append(x1)
    ycoordinates.append(y1)

plt.plot(xcoordinates, ycoordinates)

#Naming the Axis
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

#Graph title
plt.title("Digital Differential Analyzer (DDA) Algorithm")

#show the plot

plt.show()
