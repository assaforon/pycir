# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=range(1,6)
y=[1/7,1/8,1/2,1/4,4/17]
wt=[7,24,20,12,17]

fig, ax = plt.subplots()
ax.scatter(x,y,wt,c='black',marker='x')