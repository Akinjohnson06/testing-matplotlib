#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]


# In[37]:


plt.plot(yield_apples);


# In[4]:


years = [2010, 2011, 2012, 2013, 2014, 2015]
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]


# In[5]:


plt.plot(years, yield_apples);


# # AXIS LABEL

# In[41]:


plt.plot(years, yield_apples)
plt.xlabel('Years')
plt.ylabel('Yield_apples');


# # PLOTTING MULTIPLE LINES

# In[39]:


years = range(2000, 2012)
apples = [6, 5, 4, 9, 3, 1, 7, 10, 8, 2, 4, 8]
oranges = [10, 5, 2, 4, 6, 8, 7, 3, 9, 1, 7, 2]
pineapple = [10, 5, 2, 2, 6, 9, 7, 1, 9, 2, 7, 2]


# In[27]:


years = range(2000, 2012)
apples_r = random.sample(range(1, 11), 12)
oranges_r = random.sample(range(1, 11), 12)


# In[42]:


plt.plot(years, apples)
plt.plot(years, oranges)
plt.plot(years, pineapple)
plt.xlabel('Years') #labels Xaxis
plt.ylabel('Yield'); #labels Yaxis


# # Chat Titles and Legend
# 

# In[16]:


plt.plot(years, apples)
plt.plot(years, oranges)

plt.xlabel('Years')
plt.ylabel('Yield')

plt.title('Quantity of Fruits per Year') #applies to all the chats
plt.legend(['apples', 'oranges']);


# # Line Markers
# [Learn about more markers](https://matplotlib.org/stable/api/markers_api.html)
# 
# there are so many types of marker... In this image, i used only two markers
# 

# In[17]:


plt.plot(years, apples, marker='x')
plt.plot(years, oranges, marker='.')

plt.xlabel('Years')
plt.ylabel('Yield')

plt.title('Quantity of Fruits per Year') #applies to all the chats
plt.legend(['apples', 'oranges']);


# # Styling Lines and Markers
# [Learn about more colors1](https://matplotlib.org/stable/users/explain/colors/colors.html)
# 
# [Learn about more colors2](https://matplotlib.org/stable/gallery/color/named_colors.html)

# In[22]:


plt.plot(years, apples, marker='x', c='b', ls='-')
plt.plot(years, oranges, marker='x', c='y', ls='--')

plt.xlabel('Years')
plt.ylabel('Yield')

plt.title('Quantity of Fruits per Year') #applies to all the chats
plt.legend(['apples', 'oranges']);


# In[24]:


# A shorthand to specify marker, line and colour
# format = '[marker][line][colour]'

plt.plot(years, apples, 's-b') #s is the marker, - is the type of line and b is the colour of the line
plt.plot(years, oranges, 'x--r')#x is the marker, -- is the type of line and r is the colour of the line

plt.xlabel('Years')
plt.ylabel('Yield')

plt.title('Quantity of Fruits per Year') #applies to all the chats
plt.legend(['apples', 'oranges']);


# In[44]:


# or you might decide not to add lines at all by not specifying the line type
plt.plot(years, apples, 'sb') #s is the marker, - is the type of line and b is the colour of the line
plt.plot(years, oranges, 'xr')#x is the marker, -- is the type of line and r is the colour of the line

plt.xlabel('Years')
plt.ylabel('Yield')

plt.title('Quantity of Fruits per Year') #applies to all the chats
plt.legend(['apples', 'oranges']);


# # Changing the size of the graph

# In[51]:


plt.figure(figsize=(8,5))

plt.plot(years, apples, 's-b') #s is the marker, - is the type of line and b is the colour of the line
plt.plot(years, oranges, 'x--r')#x is the marker, -- is the type of line and r is the colour of the line

plt.xlabel('Years')
plt.ylabel('Yield')

plt.title('Quantity of Fruits per Year') #applies to all the chats
plt.legend(['apples', 'oranges']);


# # Improving default styles using seaborn

# In[ ]:




