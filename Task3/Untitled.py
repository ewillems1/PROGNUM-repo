#!/usr/bin/env python
# coding: utf-8

# In[27]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]
newmasses=[]
for i in masses:
    if i> 7.349e+22:
        newmasses.append(i)
print(newmasses)

print(masses[:5])
Sum=sum(masses[:5])
n=len(masses[:5])
average=Sum/n
print(average)


# In[ ]:




