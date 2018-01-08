#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
from shapely.geometry import Polygon

def circle(c,r):
 xi, xf = c[0]-r, c[0]+r
 X = np.linspace(xi,xf,500)
 Y1 = np.sqrt(r**2-np.power(X-c[0],2)) + c[1]
 Y2 = -np.sqrt(r**2-np.power(X-c[0],2)) + c[1]
 return  plt.plot(X,Y1,'k'), plt.plot(X,Y2,'k')
