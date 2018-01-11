#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
import math as mt
from shapely.geometry import Polygon
import randpoly as rp
from circle import *

#rmax, rmin, pi = 0, 1e30, mt.pi
pi = mt.pi
cont = 0
for i in range (10):
 [Poly, [x, y], Area] = rp.randpolygon()
 area, xi, yi, x_c, y_c = 0, x[0], y[0], 0, 0
 rmin, rmax = 1e30, 0.
 for i,j in zip(x[1:],y[1:]):
  area = area + (i + xi) * (j - yi) 
  x_c = x_c + (i + xi)*(xi*j - yi*i)
  y_c = y_c + (j + yi)*(xi*j - yi*i)
  xi, yi = i, j
 area = abs(area/2)
 bary = [abs(x_c)/(6*area), abs(y_c)/(6*area)] 
 for i,j in zip(x,y):
  rmax = max([rmax,mt.sqrt((i-bary[0])**2+(j-bary[1])**2)])
  rmin = min([rmin,mt.sqrt((i-bary[0])**2+(j-bary[1])**2)])

 if pi*rmin**2<area<pi*rmax**2:
  print "True"
 else:
  print "False"
  plt.figure(cont)
  circle(bary,rmin)
  circle(bary,rmax)
  plt.plot(bary[0], bary[1], '.')
  plt.axes().set_aspect('equal', 'datalim')
  plt.savefig('./'+str(cont+1))
  cont+=1
 plt.close()
print cont

#*************************
