from random import seed, uniform
from math import pi, cos, sin, tan
from numpy import array,arange
from numpy.linalg import norm

seed()

def gammamc(r,X):
    hits = 0.0
    total = 0
    while total < X:
          x = uniform(-(r+0.5),r+0.5)
          y = uniform(-(r+0.5),r+0.5)
          theta = uniform(0,2*pi)
          e1 = array([x,y]) + r/2 * array([cos(theta),sin(theta)])
          e2 = array([x,y]) - r/2 * array([cos(theta),sin(theta)])
          if isOutOfBounds(r,e1) | isOutOfBounds(r,e2): continue
          if isInSubarray(e1) | isInSubarray(e2): hits+=1
          else:
             m = tan(theta)
             k = y - m*x
             l = (lambda x: m*x + k)
             invl = (lambda y: (y - k)/m)
             a = [-0.5,l(-0.5)]
             b = [0.5,l(0.5)]
             c = [invl(0.5),0.5]
             d = [invl(-0.5),-0.5]
             isOnLine = (lambda pt: (min(e1[0],e2[0]) <= pt[0]) 
                                and (pt[0] <= max(e1[0],e2[0])) 
                                and (min(e1[1],e2[1]) <= pt[1])
                                and (pt[1] <= max(e1[1],e2[1])) )
             if (    (isOnLine(a) and isInSubarray(a))
                  or (isOnLine(b) and isInSubarray(b))
                  or (isOnLine(c) and isInSubarray(c))
                  or (isOnLine(d) and isInSubarray(d))): hits += 1
          total+=1
    return hits/X

def isOutOfBounds(r,pt):
    x,y=pt
    if (    (x <= -(r + 0.5)) or (r + 0.5 <= x)
         or (y <= -(r + 0.5)) or (r + 0.5 <= y) ): return True
    for cr,sa in [[array([xo*(r+0.5),yo*(r+0.5)]),
                   array([xo*0.5,yo*0.5])] for xo in [-1,1] 
                                           for yo in [-1,1]]:
        if ((norm(pt-cr) <= r) and (r <= norm(pt-sa))): return True
    return False

def isInSubarray(pt):
    x,y=pt
    return (     (-0.5 <= x) and (x <= 0.5) 
             and (-0.5 <= y) and (y <= 0.5) )

import os
fp = open("gammamc.tsv","w")
for x in arange(0,100,0.01): 
     fp.write("%g\t%f\n" % (x,gammamc(x,1000)))
     fp.flush()
     os.fsync(fp)
 fp.close()
