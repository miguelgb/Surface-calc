#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
import math as mt
from shapely.geometry import Polygon

#This program makes a random polygon, which vetex number may
#vary between 3 and 10

def randpolygon():
 npoints =  random.randrange(3, 10)
 print "Generating",npoints,"\b-vertex polygon..."
 points, vert = np.random.rand(2,npoints), []
 max_length = 100

 def length(vertix):
  polygon = Polygon(vertix)
  return polygon.length

 for i,j in zip(points[0],points[1]):
  vert.append((i,j))

 for i in range(mt.factorial(npoints)):
  if max_length > length(vert):
   max_length = length(vert)
   op_vert = vert
  vert = np.random.permutation(vert)

 polygon = Polygon(op_vert)
# print "Area =", polygon.area
 x,y = polygon.exterior.xy
 return plt.plot(x,y, color='#6699cc', alpha=0.7,linewidth=3,
                 solid_capstyle='round', zorder=2), [x,y], polygon.area



