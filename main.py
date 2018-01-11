#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
import math as mt
from shapely.geometry import Polygon
import randpoly as rp
from circle import *



[Poly, [x, y], Area] = rp.randpolygon()
area, xi, yi, x_c, y_c = 0, x[0], y[0], 0, 0
rmin, rmax = 1e30, 0.
for i,j in zip(x[1:],y[1:]):
 area = area + (i + xi) * (j - yi) 
 x_c = x_c + (i + xi)*(xi*j - yi*i)
 y_c = y_c + (j + yi)*(xi*j - yi*i)
 xi, yi = i, j
area = abs(area/2)
print "Area:",area

#22
