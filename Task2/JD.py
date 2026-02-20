#!/usr/bin/env python
# coding: utf-8

# In[2]:


D=float(input("Enter day(can be fractional):"))
M=float(input("Enter month:"))
Y=float(input("Enter year:"))

JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
print(JD)


# In[4]:


D=float(input("Enter day(can be fractional) of date 1:"))
M=float(input("Enter month of date 1:"))
Y=float(input("Enter year of date 1:"))

JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5

d=float(input("Enter day(can be fractional) of date 2:"))
m=float(input("Enter month of date 2:"))
y=float(input("Enter year of date 2:"))

jd = 367*y -7*(y+(m+9)//12)//4 - 3*((y+(m-9)//7)//100 + 1)//4 + (275*m)//9 + d + 1721029-0.5

X=jd-JD

print('number of days between two dates:')
print(X)


# In[ ]:




