#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
import math as mt
from shapely.geometry import Polygon
import randpoly as rp

cont = 0
for it in range(10000):
 [Poly, [x, y], Area] = rp.randpolygon()

 area, xi, yi = 0, x[0], y[0] 
 for i,j in zip(x[1:],y[1:]):
  area = area + (i + xi) * (j - yi) 
  xi, yi = i, j
 area = abs(area/2)
 if abs(area-Area)>1e-15:
  print "False"
  print "Area:",Area
  print "Area in sc:",area
  print "Log error:",abs(area-Area)/Area
  print Poly
  print "\n"
  cont+=1
print "Número de errores:",cont

