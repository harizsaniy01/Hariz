import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def midpoint(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Initialize the decision parameter
    d  = dy - (dx/2)
    x = x1
    y = y1

    st.header(f"X = {x}, Y = {y}")

    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    while (x<x2):
        x = x + 1

        # East is Chosen
        if (d<0):
            d = d + dy

        # North East is Chosen
        else:
            d = d + (dy - dx)
            y = y + 1

        xcoordinates.append(x)
        ycoordinates.append(y)
        st.header(f"X = {x}, Y = {y}")
        
    fig = plt.figure(figsize=(10, 4))
    plt.title("Midpoint Line Algorithm")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.plot(xcoordinates, ycoordinates)
    plt.show()
    st.pyplot(fig)
    
if __name__=="__main__":
    x1 = int(input("Enter the Starting Point of X: "))
    y1 = int(input("Enter the Starting Point of Y: "))
    x2 = int(input("Enter the End Point of X: "))
    y2 = int(input("Enter the End Point of Y: "))

    midpoint(x1, y1, x2, y2)
