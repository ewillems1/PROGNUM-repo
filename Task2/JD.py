#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ask the user for a day, month, and year, allowing for fractional days
D=float(input("Enter day(can be fractional):"))
M=float(input("Enter month:"))
Y=float(input("Enter year:"))

# Compute the Julian Date using the standard astronomical formula
JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5

# Display the resulting Julian Date
print(JD)


# In[2]:


# Ask the user for the first date
D=float(input("Enter day(can be fractional) of date 1:"))
M=float(input("Enter month of date 1:"))
Y=float(input("Enter year of date 1:"))

# Compute the Julian Date of the first date
JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5

# Ask the user for the second date
d=float(input("Enter day(can be fractional) of date 2:"))
m=float(input("Enter month of date 2:"))
y=float(input("Enter year of date 2:"))

# Compute the Julian Date of the second date
jd = 367*y -7*(y+(m+9)//12)//4 - 3*((y+(m-9)//7)//100 + 1)//4 + (275*m)//9 + d + 1721029-0.5

# Compute and print the number of days between the two dates
X=jd-JD
print(f"number of days between two dates:{X}")


# In[ ]:




