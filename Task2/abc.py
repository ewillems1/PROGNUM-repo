#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import *
a=float(input("enter a:"))
b=float(input("enter b:"))
c=float(input("enter c:"))

if a==0:
    if b==0:
        if c==0:
            print("infinitely many solutions")
        else:
            print("no solutions")
    else:
        x=-c/b
        print("solution:", x)
else:
    D=b**2-4*a*c
    if D<0:
        print("no real solutions")
    elif D==0:
        x1=(-1* b + sqrt(D))/(2*a)
        print("one solutio:",x1)
    else:
        x1=(-1* b + sqrt(D))/(2*a)
        x2=(-1*b - sqrt(D))/(2*a)
        print("two solutions:",x1,"and",x2)


# In[ ]:




